from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utilities import generation_token, get_phone, get_otp
from rest_framework.response import Response
from rest_framework import status
from .models import User, BaseProduct, Region, Category, AdditonalImage
from .serializers import UserSerializer, BaseProductSerializer, RegionSerializer, CategorySerializer
from .serializers import UserAdSerializer, CommonProductDetail, UserFavoriteSerializer
import hashlib, os
from slugify import slugify
from random import randint
from .middleware import serializer_save, get_add_detail, serializer_edit, serializer_get_edit, ad_filter_by_category
from .choices import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging

@api_view(['POST'])
@permission_classes([AllowAny,])
def send_sms(request):
	phone_number = request.data.get('phone_number')
	if phone_number:
		data = get_phone(phone_number)
	return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny,])
def authentification_user(request):
	user_otp = request.data.get('otp')
	phone_number = request.data.get('phone_number')
	otp_key = request.data.get('otp_key')
	if phone_number and user_otp and otp_key:
		data = get_otp(user_otp, otp_key)
		if data['Status'] == "Success":
			if User.objects.filter(phone_number=phone_number).exists():
				user = User.objects.get(phone_number=phone_number)
				user_details = generation_token(user, request)
			else:
				user = User.objects.create_user(phone_number=phone_number)
				user.save()
				user_details = generation_token(user, request)
			return Response(user_details, status=status.HTTP_200_OK)
		else:
			return Response(data)
	else:
		return Response(request.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def profile(request):
	serializer = UserSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def add_remove_favorites(request):
	product = BaseProduct.objects.get(id=request.data.get('product_id'))
	if product.favorite_for.filter(id=request.user.id).exists():
		product.favorite_for.remove(request.user)
	else:
		product.favorite_for.add(request.user)
	return Response(product.id, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny,])
def category(request):
	categories = Category.objects.all()
	if (request.query_params.get('lft') and request.query_params.get('rght')):
		categories = categories.filter(lft__gte=request.query_params.get('lft'), rght__lte=request.query_params.get('rght'))
	if (request.query_params.get('level')):
		categories = categories.filter(level=request.query_params.get('level'))
	if (request.query_params.get('tree_id')):
		categories = categories.filter(tree_id=request.query_params.get('tree_id'))
	serializer = CategorySerializer(categories, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny,])
def region(request):
	categories = Region.objects.all()
	if (request.query_params.get('lft') and request.query_params.get('rght')):
		categories = categories.filter(lft__gte=request.query_params.get('lft'), rght__lte=request.query_params.get('rght'))
	if (request.query_params.get('level')):
		categories = categories.filter(level=request.query_params.get('level'))
	if (request.query_params.get('tree_id')):
		categories = categories.filter(tree_id=request.query_params.get('tree_id'))
	serializer = RegionSerializer(categories, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def get_region_id(request):
	region = Region.objects.get(id=request.query_params.get('id'))
	serializer = RegionSerializer(region)
	return Response(serializer.data, status=status.HTTP_200_OK)





@api_view(['GET'])
@permission_classes([AllowAny,])
def ad_filter(request, region=None, category=None):
	logging.error(request.user)
	obj_region = Region.objects.get(slug=region)
	if (category):
		obj_category = Category.objects.get(slug=category)
		ad_list = ad_filter_by_category(request, obj_region, obj_category)  # Filter ad_lsit by additional params
	else:
		ad_list = BaseProduct.objects.filter(region__lft__gte=obj_region.lft, region__rght__lte=obj_region.rght)


	if(request.query_params.get('priceFrom')):
		ad_list = ad_list.filter(price__gte=request.query_params.get('priceFrom'))
	if(request.query_params.get('priceUp')):
		ad_list = ad_list.filter(price__lte=request.query_params.get('priceUp'))
	if (request.query_params.get('order')):
		if (request.query_params.get('order') == 'priceMinus'):
			ad_list = ad_list.order_by('price')
		elif (request.query_params.get('order') == 'pricePlus'):
			ad_list = ad_list.order_by('-price')


	paginator = Paginator(ad_list, 25)
	page = request.GET.get('page')
	try:
		ads = paginator.page(page)
	except PageNotAnInteger:
		ads = paginator.page(1)
	except EmptyPage:
		return Response(status=status.HTTP_204_NO_CONTENT)
	serializer = BaseProductSerializer(ads, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)





@api_view(['GET'])
@permission_classes([AllowAny,])
def add_detail(request, region,category, slug):
	data = get_add_detail(request ,region,category,slug)
	return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny,])
def user_detail(request, user):
	usr = User.objects.get(id=user)
	serializer = UserSerializer(usr)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def get_user_ad(request):
	serializer = UserAdSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def get_user_favorites(request):
	serializer = UserFavoriteSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def add_ad(request):
	serializer = serializer_save(request)
	if serializer.is_valid():
		slug = slugify(serializer.validated_data['title']) + '-' + str(randint(1000,9999))
		serializer.save(slug=slug)
		product = BaseProduct.objects.get(slug=slug)
		images = dict((request.data).lists())['images[]']
		for img in images:
			AdditonalImage.objects.create(baseproduct=product, image=img)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors)

@api_view(['PUT', 'GET', 'DELETE'])
@permission_classes([IsAuthenticated,])
def edit_ad(request, slug):
	if request.method == 'PUT':
		serializer = serializer_edit(request,slug)
		if serializer.is_valid():
			slug = slugify(serializer.validated_data['title']) + '-' + str(randint(1000,9999))
			serializer.save(slug=slug)
			product = BaseProduct.objects.get(slug=slug)
			images_product = product.images.all()
			if(images_product):
				for img in images_product:
					img.delete()
			if (dict((request.data).lists())['images[]']):
				images = dict((request.data).lists())['images[]']
				for img in images:
					AdditonalImage.objects.create(baseproduct=product, image=img)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors)
	elif request.method == 'GET':
		serializer = serializer_get_edit(request,slug)
		return Response(serializer, status=status.HTTP_200_OK)
	elif request.method == 'DELETE':
		product = BaseProduct.objects.get(slug=slug)
		if (product.user_id == request.user.id):
			response = u'Successful delete product {}'.format(product.title)
			product.delete()
		return Response(response)

@api_view(['PUT'])
@permission_classes([IsAuthenticated,])
def active_ad(request, slug):
	product = BaseProduct.objects.get(slug=slug)
	if (product.is_active):
		product.is_active = False
	else:
		product.is_active = True
	product.save()
	serializer = BaseProductSerializer(product)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny,])
def get_choices(request):
	available_dicts = {
		"NUMBER_ROOMS": NUMBER_ROOMS,
		"MARK": MARK,
		"GEAR_SHIFT":GEAR_SHIFT,
		"BODY_TYPE": BODY_TYPE,
		"ENGINE_TYPE": ENGINE_TYPE,
		"DRIVE_UNIT": DRIVE_UNIT,
		"SCHEDULE": SCHEDULE,
		"WORK_EXPERIENCE": WORK_EXPERIENCE
	}
	choices = request.query_params.get('choices')
	if choices is not None and choices in available_dicts:
		result_list = []
		chosen_dict = available_dicts[choices]
		result_list = chosen_dict
		return Response(result_list, status=status.HTTP_200_OK)
	else:
		return Response({'Error': 'Empty or invalid choice given'}, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

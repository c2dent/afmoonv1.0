from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utilities import generation_token, get_phone, get_otp
from rest_framework.response import Response
from rest_framework import status
from .models import User, BaseProduct, Region, Category, AdditonalImage
from .serializers import UserSerializer, BaseProductSerializer, RegionSerializer, CategorySerializer, AdditonalImageSerializer
import hashlib, os
from slugify import slugify
from random import randint
from .middleware import serializer_save, get_add_detail
from .choices import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
				return Response(user_details, status=status.HTTP_200_OK)
			else:
				user = User.objects.create_user(phone_number=phone_number)
				user.save()
				user_details = generation_token(user, request)
				return Response(user_details, status=status.HTTP_200_OK)
		else:
			return Response({'Message':'Failed'})
	else:
		return Response(request.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def profile(request):
	serializer = UserSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def category(request):
	if (request.query_params.get('lft') and request.query_params.get('rght') and request.query_params.get('level')):
		categories = Category.objects.filter(lft__gte=request.query_params.get('lft'), rght__lte=request.query_params.get('rght'), level=request.query_params.get('level'))
	elif (request.query_params.get('tree_id')):
		categories = Category.objects.filter(tree_id=request.query_params.get('tree_id'))
	elif (request.query_params.get('level')):
		categories = Category.objects.filter(level=request.query_params.get('level'))
	elif (request.query_params.get('lft') and request.query_params.get('rght')):
		categories = Category.objects.filter(lft__gte=request.query_params.get('lft'), rght_lte=request.query_params.get('rght'))
	else:
		serializer = request
	serializer = CategorySerializer(categories, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def region(request):
	if (request.query_params.get('lft') and request.query_params.get('rght') and request.query_params.get('level')):
		regions = Region.objects.filter(lft__gte=request.query_params.get('lft'), rght__lte=request.query_params.get('rght'), level=request.query_params.get('level'))
	elif (request.query_params.get('tree_id')):
		regions = Region.objects.filter(tree_id=request.query_params.get('tree_id'))
	elif (request.query_params.get('level')):
		regions = Region.objects.filter(level=request.query_params.get('level'))
	elif (request.query_params.get('lft') and request.query_params.get('rght')):
		regions = Region.objects.filter(lft__gte=request.query_params.get('lft'), rght_lte=request.query_params.get('rght'))
	else:
		serializer = request
	serializer = RegionSerializer(regions, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([AllowAny,])
def by_region(request, region=None):
	region = Region.objects.get(slug=region)
	ad_list = BaseProduct.objects.filter(region__lft__gte=region.lft, region__rght__lte=region.rght)
	paginator = Paginator(ad_list, 25)
	page = request.GET.get('page')
	try:
		ads = paginator.page(page)
	except PageNotAnInteger:
		ads = paginator.page(1)
	except EmptyPage:
		ads = paginator.page(paginator.num_pages)
	serializer = BaseProductSerializer(ads, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny,])
def by_region_category(request, region=None, category=None):
	obj_region = Region.objects.get(slug=region)
	obj_category = Category.objects.get(slug=category)
	ad_list = BaseProduct.objects.filter(region__lft__gte=obj_region.lft, region__rght__lte=obj_region.rght,
										category__lft__gte=obj_category.lft, category__rght__lte=obj_category.rght)
	paginator = Paginator(ad_list, 25)
	page = request.GET.get('page')
	try:
		ads = paginator.page(page)
	except PageNotAnInteger:
		ads = paginator.page(1)
	except EmptyPage:
		ads = paginator.page(paginator.num_pages)
	serializer = BaseProductSerializer(ads, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny,])
def add_detail(request, region,category, slug):
	data = get_add_detail(region,category,slug)
	return Response(data, status=status.HTTP_200_OK)

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
		"WORK_EXPERIENCE": WORK_EXPERIENCE,
		"SIZE_CLOTHES": SIZE_CLOTHES,
		"SIZE_SHOES": SIZE_SHOES,
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
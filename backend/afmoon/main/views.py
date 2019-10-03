from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utilities import generation_token, get_phone, get_otp
from rest_framework.response import Response
from rest_framework import status
from .models import User, BaseProduct, Region, Category
from .serializers import UserSerializer, BaseProductSerializer, RegionSerializer, CategorySerializer
import hashlib, os
from .middleware import serialzier_save


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
@permission_classes([AllowAny,])
def region(request):
	regions = Region.objects.filter(lft__gte=request.data.get('lft'), rght_lte=request.data.get('rght'))
	serializer = RegionSerializer(regions, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def category(request):
	if (request.query_params.get('tree_id')):
		categories = Category.objects.filter(tree_id=request.query_params.get('tree_id'))
	elif (request.query_params.get('level')):
		categories = Category.objects.filter(level=request.query_params.get('level'))
	elif (request.query_params.get('lft') or request.query_params.get('rght')):
		categories = Category.objects.filter(lft__gte=request.query_params.get('lft'), rght_lte=request.query_params.get('rght'))
	else:
		serializer = request
	serializer = CategorySerializer(categories, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny,])
def by_region(request):
	region = Region.objects.get(slug=request.data.get('region'))
	ad_list = BaseProduct.objects.filter(region__lft__gte=region.lft, region__rght__lte=region.rght)
	serializer = BaseProductSerializer(ad_list, many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def add_ad(request):
	serializer = serializer_save(request)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.

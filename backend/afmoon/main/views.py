from django.shortcuts import render
from django.conf import settings
import requests
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from .utilities import generation_token
from rest_framework.response import Response
from rest_framework import status
from .models import User


@api_view(['POST'])
@permission_classes([AllowAny,])
def send_sms(request):
	phone_number = request.data.get(phone_number, None)
	url = "http://2factor.in/API/V1/" + settings.API_KEY + "/SMS/" + phone_number + "/AUTOGEN/OTPSEND"
	if phone_number:
		response = requests.request("GET", url)
		data = response.json()
		request.session['otp_session_data'] = data['Details']
		response_data = {'Message': 'Succes'}
	else:
		response_data = {'Message': 'Failed'}
	return Response(response_data)


@api_view(['POST'])
@permission_classes([AllowAny,])
def authentification_user(request):
	user_otp = request.data.get(otp, None)
	phone_number = request.data.get(phone_number, None)
	if user_otp:
		url = "http://2factor.in/API/V1/" + settings.API_KEY + "/SMS/VERIFY/" + request.session['otp_session_data'] + "/" + user_otp + ""
		response = requests.request("GET", url)
		data = response.json()
		if data['Status'] == "Succes":
			if User.objects.get(phone_number=phone_number):
				user_details = generation_token(User.objects.get(phone_number=phone_number), request)
				return Response(user_details, status=status.HTTP_200_OK)
			else:
				user = User.objects.create_user(phone_number=phone_number)
				user.save()
				user_details = generation_token(user, request)
				return Response(user_details, status=status.HTTP_200_OK)
		else:
			return Response({'Message':'Failed'})
	else:
		return Response({'Message': 'Wrong otp'})

# Create your views here.

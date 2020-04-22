from django.contrib.auth.signals import user_logged_in
from rest_framework_jwt.settings import api_settings
from django.conf import settings
from datetime import datetime
from os.path import splitext
import requests
import jwt



jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER

def generation_token(user, request):
	try:
		payload = jwt_payload_handler(user)
		token = jwt.encode(payload, settings.SECRET_KEY)
		user_details = {}
		user_details['token'] = token
		user_logged_in.send(sender=user.__class__,request=request, user=user)
		return user_details
	except Exception as e:
		raise e


def get_phone (phone_number):
	url = 'http://2factor.in/API/V1/' + settings.API_KEY + '/SMS/' + phone_number + '/AUTOGEN/OTPSEND'
	response = requests.request("GET", str(url))
	data = response.json()
	return data

def get_otp (otp, otp_key):
	url = "http://2factor.in/API/V1/" + settings.API_KEY + "/SMS/VERIFY/" + otp_key + "/" + otp + ""
	response = requests.request("GET", url)
	data = response.json()
	return data

def get_timestamp_path(instanse, filename):
	return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
from django.contrib.auth.signals import user_logged_in
from rest_framework_jwt.settings import api_settings
from django.conf import settings
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
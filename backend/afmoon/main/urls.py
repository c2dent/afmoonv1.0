from django.urls import path
from .views import send_sms, authentification_user

urlpatterns = [
	path('accounts/send-sms/', send_sms),
	path('accounts/confirm-phone/', authentification_user)
]
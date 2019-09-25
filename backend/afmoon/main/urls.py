from django.urls import path
from .views import send_sms, authentification_user,profile, by_region

urlpatterns = [
	path('accounts/send-sms/', send_sms),
	path('accounts/confirm-phone/', authentification_user),
	path('accounts/profile/', profile),
	path('<slug:region>/', by_region)
]
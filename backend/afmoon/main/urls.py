from django.urls import path
from .views import send_sms, authentification_user,profile, by_region, add_ad, region, category

urlpatterns = [
	path('accounts/send-sms/', send_sms),
	path('accounts/confirm-phone/', authentification_user),
	path('accounts/profile/', profile),
	path('category/', category),
	path('region/', region),
	path('add_ad/', add_ad),
	path('<slug:region>/', by_region)
]
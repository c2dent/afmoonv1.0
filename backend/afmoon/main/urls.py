from django.urls import path
from .views import send_sms, authentification_user,profile, by_region, add_ad, region, category, get_choices,by_region_category, add_detail, user_detail
from .views import get_user_ad, edit_ad, get_region_id, active_ad, ad_filter

urlpatterns = [
	path('accounts/send-sms/', send_sms),
	path('accounts/confirm-phone/', authentification_user),
	path('accounts/profile/', profile),
	path('category/', category),
	path('region-id/', get_region_id),
	path('region/', region),
	path('add-ad/', add_ad),
	path('edit-ad/active/<slug:slug>/', active_ad),
	path('edit-ad/<slug:slug>/', edit_ad),
	path('user-ads/', get_user_ad),
	path('choices/', get_choices),
	path('user/<slug:user>/', user_detail),
	path('<slug:region>/<slug:category>/<slug:slug>/', add_detail),
	path('<slug:region>/<slug:category>/', ad_filter),
	path('<slug:region>/', ad_filter)
]
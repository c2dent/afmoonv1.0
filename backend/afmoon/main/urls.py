from django.urls import path
from .views import send_sms, authentification_user,profile, get_choices, user_detail, ProductList, AdCreateAPIView
from .views import get_user_ad, active_ad, add_remove_favorites, get_user_favorites, CategoryList, RegionList, AdDetail

urlpatterns = [
	path('accounts/send-sms/', send_sms),
	path('accounts/confirm-phone/', authentification_user),
	path('accounts/profile/', profile),
	path('accounts/add-remove-favorite/', add_remove_favorites),
	path('accounts/user-favorites/', get_user_favorites),
	path('category/', CategoryList.as_view()),
	path('region/', RegionList.as_view()),
	path('add-ad/', AdCreateAPIView.as_view()),
	path('edit-ad/active/<slug:slug>/', active_ad),
	path('user-ads/', get_user_ad),
	path('choices/', get_choices),
	path('ads/', ProductList.as_view()),
	path('ads/<slug:slug>/', AdDetail.as_view()),
	path('user/<slug:user>/', user_detail),
]
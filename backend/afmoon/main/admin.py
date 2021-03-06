from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm, UserCreationForm, LoginForm
from mptt.admin import MPTTModelAdmin

from moderation.admin import ModerationAdmin

from .models import User, Region, Category, BaseProduct, Apartment, Avtomobil, AdditonalImage
from .models import House, Land, Vacancy, Resume

class UserAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm
	login_form = LoginForm

	list_display = [
		'phone_number',
		'nickname',
		'is_admin',
	]
	list_filter = ('is_admin',)

	fieldsets = (
				(None, {'fields': ('phone_number',)}),
				('Personal info',{
				'fields': (
					'avatar',
					'nickname',
					'region',
					)}),
				('Permissions', {'fields': ('is_admin',)}),
				('Important dates', {'fields': ('last_login',)}),
		)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': (
					'phone_number',
				)
			}),
	)

	search_fields = ('phone_number',)
	ordering = ('phone_number',)
	filter_horizontal = ()

class AdditonalImageAdmin(admin.ModelAdmin):
	fields = ['image', 'baseproduct']

class RegionAdmin(MPTTModelAdmin):
	fields = ['title', 'parent', 'slug']

class CategoryAdmin(MPTTModelAdmin):
	fields = ['title', 'parent', 'slug']

class BaseProductAdmin(admin.ModelAdmin):
	fields = ['title', 'price', 'region', 'slug', 'description', 'category', 'views', 'is_active', 'user', 'favorite_for']

	list_display = [
		'title',
		'price',
		'id'
	]

	search_fields = ('slug',)
	ordering = ('slug',)
	filter_horizontal = ()

class AvtomobilAdmin(BaseProductAdmin):
	fields = BaseProductAdmin.fields + ['mark_model', 'year_issue', 'gear_shift', 'body_type', 'engine_type', 'mileage', 'drive_unit', 'condition']

class ApartmentAdmin(BaseProductAdmin):
	fields = BaseProductAdmin.fields + ['floors_in_house', 'floor', 'number_rooms', 'total_area' ,'rent_buy']

class HouseAdmin(BaseProductAdmin):
	fields = BaseProductAdmin.fields + ['house_area', 'land_area']

class LandAdmin(BaseProductAdmin):
	fields = BaseProductAdmin.fields + ['land_area']

class VacancyAdmin(BaseProductAdmin):
	fields = BaseProductAdmin.fields + ['schedule', 'work_experience']

class ResumeAdmin(BaseProductAdmin):
	fields = BaseProductAdmin.fields + ['gender', 'age', 'schedule', 'work_experience']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(BaseProduct, BaseProductAdmin)
admin.site.register(AdditonalImage, AdditonalImageAdmin)
admin.site.register(Avtomobil, AvtomobilAdmin)
admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(Land, LandAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

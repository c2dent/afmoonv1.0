from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm, UserCreationForm, LoginForm

from .models import User

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
					'register_date',
					'nickname',
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


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
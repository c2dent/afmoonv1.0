from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

class UserCreationForm(forms.ModelForm):
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		if commit:
			user.save()
		return user

	class Meta:
		model = get_user_model()
		fields = ('phone_number',)

class UserChangeForm(forms.ModelForm):
	def save(self, commit=True):
		user = super(UserChangeForm, self).save(commit=False)
		if commit:
			user.save()
		return user

	class Meta:
		model = get_user_model()
		fields = ['phone_number', ]

class LoginForm(forms.Form):
	username = forms.CharField()
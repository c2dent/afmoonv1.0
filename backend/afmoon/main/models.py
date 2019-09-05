from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
	def create_user(self, phone_number):
		if not phone_number:
			raise ValueError('Номер телефона обьязательно должен быть указан')
		user = self.model(
				phone_number = phone_number,
			)
		user.save(using=self._db)
		return user

	def create_superuser(self, phone_number,password):
		if not phone_number:
			raise ValueError('Номер телефона обьязательно должен быть указан')

		user = self.model(phone_number=phone_number,is_superuser=True)
		user.set_password(password)
		user.is_admin = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser, PermissionsMixin):
	phone_number = models.CharField('телефон номер', max_length=20, unique=True,db_index=True)
	avatar = models.ImageField('Аватар', blank=True, null=True, upload_to='user/avatar')
	nickname = models.CharField('Никнейм', max_length=40, null=True, blank=True)
	register_date = models.DateField('Дата регистрация', auto_now_add=True)
	is_active = models.BooleanField('Активен', default=True)
	is_admin = models.BooleanField('Суперпользователь', default=False)

	def get_full_name(self):
		return self.phone_number

	def is_staff(self):
		return self.is_admin

	def get_short_name(self):
		return self.phone_number

	def __str__(self):
		return self.phone_number

	USERNAME_FIELD = 'phone_number'
	REQUIRED_FIELDS = []

	objects = UserManager()

	class Meta:
		verbose_name= 'User'
		verbose_name_plural = 'Users'
# Create your models here.

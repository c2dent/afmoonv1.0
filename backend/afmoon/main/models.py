from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from .utilities import get_timestamp_path
from .choieces import *

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

class Region(MPTTModel):
	title = models.CharField("Регион", max_length=50, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
	slug = models.SlugField(max_length=50, blank=True)

	class Meta:
		verbose_name = ("Region")
		verbose_name_plural = ("Regions")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Region, self).save(*args, **kwargs)

	def __str__(self):
		return self.title


class User(AbstractBaseUser, PermissionsMixin):
	phone_number = models.CharField('телефон номер', max_length=20, unique=True,db_index=True)
	avatar = models.ImageField('Аватар', blank=True, null=True, upload_to=get_timestamp_path, default='images/user.png')
	nickname = models.CharField('Никнейм', max_length=40, null=True, blank=True)
	register_date = models.DateField('Дата регистрация', auto_now_add=True)
	is_active = models.BooleanField('Активен', default=True)
	is_admin = models.BooleanField('Суперпользователь', default=False)
	region = models.ForeignKey(Region, verbose_name="", on_delete=models.CASCADE, null=True, blank=True)

	def save(self, *args, **kwargs):
		super(User, self).save(*args, **kwargs)
		self.nickname = 'User' + str(self.id)
		super(User, self).save(*args, **kwargs)

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

class Category(MPTTModel):
	title = models.CharField("Категоры", max_length=50, unique=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
	slug = models.SlugField(max_length=50, blank=True)

	class Meta:
		verbose_name = ("Categories")
		verbose_name_plural = ("Categories")

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

class BaseProduct(models.Model):
	title = models.CharField("Названия", max_length=40)
	add_date = models.DateTimeField("Дата добавления", auto_now_add=True)
	description = models.TextField("Описания", blank=True, null=True)
	image = models.ImageField("Изображения", blank=True, upload_to=get_timestamp_path, null=True)
	price = models.FloatField("Цена", blank=True, null=True)
	is_active = models.BooleanField("Is_Active", default=True, db_index=True)
	views = models.IntegerField("Просмотрый", default=0)
	category = models.ForeignKey('Category', related_name='ad', on_delete=models.PROTECT, blank=True)
	region = models.ForeignKey('Region', related_name='ad', on_delete=models.PROTECT, blank=True)
	user = models.ForeignKey('user', verbose_name="Владелес", on_delete=models.CASCADE, related_name='ad')
	slug = models.SlugField(max_length=50, blank=True)


	def delete(self, *args, **kwargs):
		for ai in self.additionalimage_set.all():
			ai.delete()
		super().delete(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Объявления'
		verbose_name = 'Объявление'
		ordering = ['-add_date']

class AdditonalImage(models.Model):
	baseproduct = models.ForeignKey("BaseProduct", verbose_name="Объявления", on_delete=models.CASCADE, related_name='images')
	image = models.ImageField(upload_to=get_timestamp_path, verbose_name='Изображения')

	class Meta:
		verbose_name_plural = 'Дополнительная иллюстрации'
		verbose_name = 'Дополнительная иллюстрация'

class Avtomobil(BaseProduct):
	mark_model = models.IntegerField('Марка и модель', choices=MARK)
	is_new = models.BooleanField("Новые или с пробегом", default=False)
	year_issue = models.IntegerField("Год выпуска")
	gear_shift = models.IntegerField('Коробка передач', choices=GEAR_SHIFT)
	body_type = models.IntegerField('Тип кузова', choices=BODY_TYPE)
	engine_type = models.IntegerField('Тип двигателя', choices=ENGINE_TYPE)
	mileage = models.IntegerField('Пробег')
	drive_unit = models.IntegerField('Привод', choices=DRIVE_UNIT)
	condition = models.BooleanField('Состояние', default=True)

class Apartment(BaseProduct):
	floors_in_house = models.IntegerField('Этажы в доме', default=0)
	floor = models.IntegerField('этаж', default=0)
	number_rooms = models.IntegerField('Количество комнат', choices=NUMBER_ROOMS)
	total_area = models.IntegerField('Общая площадь', default=1)
	rent_buy = models.BooleanField('Снять или Купить', default=True)

class House(BaseProduct):
	house_area = models.IntegerField('Площадь дома', default=1)
	land_area = models.IntegerField('Площадь участка', default=1)

class Land(BaseProduct):
	land_area = models.IntegerField('Площадь', default=1)

class Vacancy(BaseProduct):
	schedule = models.IntegerField('График работы', choices=SCHEDULE)
	work_experience = models.IntegerField('Опыть работы', choices=WORK_EXPERIENCE)

class Resume(Vacancy):
	gender = models.BooleanField("Пол", default=True)
	age = models.IntegerField("Возраст")

class Second(BaseProduct):
	second_hand = models.BooleanField("Новый или б/у", default=True)

	def __str__(self):
		return self.title

class Personals_clothes(Second):
	size = models.IntegerField("Размер", choices=SIZE_CLOTHES)

class Personals_shoes(Second):
	size = models.IntegerField("Размер", choices=SIZE_SHOES)

# Create your models here.

from rest_framework import serializers
from .models import User, BaseProduct, Avtomobil, Apartment, House, Land, Vacancy, Resume, Second, Personals_clothes, Personals_shoes
from .models import Region, Category, AdditonalImage
from .choices import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ('avatar', 'nickname', 'phone_number', 'region', 'register_date','id')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('title', 'id', 'lft', 'rght', 'tree_id', 'level','parent_id')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'id', 'lft', 'rght', 'tree_id', 'level')

class AdditonalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditonalImage
        fields = ('image',)

class BaseProductSerializer(serializers.ModelSerializer):
    region_title = serializers.ReadOnlyField(source='region.title')
    region_slug = serializers.ReadOnlyField(source='region.slug')
    category_title = serializers.ReadOnlyField(source='category.title')
    category_slug = serializers.ReadOnlyField(source='category.slug')

    class Meta:
        model = BaseProduct
        fields = ('title', 'price', 'region', 'add_date', 'slug', 'image','region_title', 'category_title', 'region_slug', 'category_slug', 'is_active')


class UserAdSerializer(serializers.ModelSerializer):
    ad = BaseProductSerializer(many=True)
    class Meta:
        model = User
        fields = ('ad',)


class CommonProductDetail(serializers.ModelSerializer):
    images = AdditonalImageSerializer(many=True, required=False)
    user_avatar = serializers.ReadOnlyField(source='user.avatar.path')
    user_phone = serializers.ReadOnlyField(source='user.phone_number')
    user_nickname = serializers.ReadOnlyField(source='user.nickname')
    user_register_date = serializers.ReadOnlyField(source='user.register_date')
    region_title = serializers.ReadOnlyField(source='region.title')
    category_title = serializers.ReadOnlyField(source='category.title')
    class Meta:
        model = BaseProduct
        fields = ('title', 'price', 'region', 'add_date', 'slug', 'description','image', 'category', 'views',
                'is_active', 'user','user_avatar', 'user_nickname','user_register_date','user_phone','images', 'region_title', 'category_title')

class AvtomobilSerializer(CommonProductDetail):
    class Meta:
        model = Avtomobil
        fields = (CommonProductDetail.Meta.fields + ('mark_model', 'year_issue', 'gear_shift', 'body_type', 'engine_type', 'mileage', 'drive_unit', 'condition'))

class ApartmentSerializer(CommonProductDetail):
    class Meta:
        model = Apartment
        fields = ((CommonProductDetail.Meta.fields) + ('floors_in_house', 'floor', 'number_rooms', 'total_area', 'rent_buy'))

class HouseSerializer(CommonProductDetail):
    class Meta:
        model = House
        fields = (CommonProductDetail.Meta.fields + ('house_area', 'land_area'))

class LandSerializer(CommonProductDetail):
    class Meta:
        model = Land
        fields = (CommonProductDetail.Meta.fields + ('land_area',))

class VacancySerializer(CommonProductDetail):
    class Meta:
        model = Vacancy
        fields = (CommonProductDetail.Meta.fields + ('schedule', 'work_experience'))

class ResumeSerializer(VacancySerializer):
    class Meta:
        model = Resume
        fields = (VacancySerializer.Meta.fields + ('gender', 'age'))

class SecondSerializer(CommonProductDetail):
    class Meta:
        model = Second
        fields = (CommonProductDetail.Meta.fields + ('second_hand',))

class PersonalsClothesSerializer(CommonProductDetail):
    class Meta:
        model = Personals_clothes
        fields = (SecondSerializer.Meta.fields + ('size',))

class PersonalsShoesSerializer(CommonProductDetail):
    class Meta:
        model = Personals_shoes
        fields = (SecondSerializer.Meta.fields + ('size',))

class TestProductSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = ('title', 'description', 'price', 'image', 'region', 'category', 'user')

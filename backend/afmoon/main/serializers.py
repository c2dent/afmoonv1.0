from rest_framework import serializers
from .models import User, BaseProduct, Avtomobil, Apartment, House, Land, Vacancy, Resume, Second, Personals_clothes, Personals_shoes
from .models import Region, Category, AdditonalImage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ('avatar', 'nickname', 'phone_number', 'region', 'register_date','id')

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('title', 'id', 'lft', 'rght', 'tree_id', 'level')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'id', 'lft', 'rght', 'tree_id', 'level')

class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = ('title', 'price', 'image', 'region', 'add_date', 'slug')

class AdditonalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditonalImage
        fields = ('baseproduct', 'image')

class CommonProductDetail(BaseProductSerializer):
    class Meta:
        model = BaseProduct
        fields = (BaseProductSerializer.Meta.fields + ('description', 'category', 'views', 'is_active', 'user'))

class AvtomobilSerialzier(CommonProductDetail):
    class Meta:
        model = Avtomobil
        fields = (CommonProductDetail.Meta.fields + ('mark_model', 'is_new', 'year_issue', 'gear_shift', 'body_type', 'engine_type', 'mileage', 'drive_unit', 'condition'))

class ApartmentSerializer(CommonProductDetail):
    class Meta:
        model = Apartment
        fields = ((CommonProductDetail.Meta.fields) + ('floors_in_house', 'floor', 'number_rooms', 'total_area', 'rent_buy'))

class HouseSerializer(CommonProductDetail):
    class Meta:
        model = House
        fields = (CommonProductDetail.Meta.fields + ('house_area', 'land_area'))

class LandSerialzier(CommonProductDetail):
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

class PersonalsClothesSerializer(SecondSerializer):
    class Meta:
        model = Personals_clothes
        fields = (SecondSerializer.Meta.fields + ('size',))

class PersonalsShoesSerializer(SecondSerializer):
    class Meta:
        model = Personals_shoes
        fields = (SecondSerializer.Meta.fields + ('size',))

class TestProductSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = ('title', 'description', 'price', 'image', 'region', 'category', 'user')

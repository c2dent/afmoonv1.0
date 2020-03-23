from rest_framework import serializers
from .models import User, BaseProduct, Avtomobil, Apartment, House, Land, Vacancy, Resume
from .models import Region, Category, AdditonalImage
from .choices import *
import logging

class UserSerializer(serializers.ModelSerializer):
    region_title = serializers.ReadOnlyField(source='region.title')
    class Meta:
        model= User
        fields= ('avatar', 'nickname', 'phone_number', 'region', 'register_date','id','region_title')


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('title', 'id', 'lft', 'rght', 'tree_id', 'level','parent_id', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'id', 'lft', 'rght', 'tree_id', 'level', 'slug')


class FilterAdditionalImage(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.all()
        minId = 2342352344232
        for img in data:
            if (img.id < minId):
                minId = img.id
        data = data.filter(id=minId)
        return super(FilterAdditionalImage, self).to_representation(data)

class AdditonalBaseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditonalImage
        list_serializer_class = FilterAdditionalImage
        fields = ('image',)


class AdditonalCommonImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditonalImage
        fields = ('image',)


class BaseProductSerializer(serializers.ModelSerializer):
    region_title = serializers.ReadOnlyField(source='region.title')
    region_slug = serializers.ReadOnlyField(source='region.slug')
    category_title = serializers.ReadOnlyField(source='category.title')
    category_slug = serializers.ReadOnlyField(source='category.slug')
    images = AdditonalBaseImageSerializer(many=True)

    class Meta:
        model = BaseProduct
        fields = ('title', 'price', 'region', 'add_date', 'slug',
            'region_title', 'category_title', 'region_slug', 'category_slug',
            'is_active', 'id', 'favorite_for', 'images')


class UserAdSerializer(serializers.ModelSerializer):
    ad = BaseProductSerializer(many=True)
    class Meta:
        model = User
        fields = ('ad',)

class UserFavoriteSerializer(serializers.ModelSerializer):
    favorites = BaseProductSerializer(many=True)
    class Meta:
        model = User
        fields = ('favorites',)


class CommonProductDetail(serializers.ModelSerializer):
    images = AdditonalCommonImageSerializer(many=True, required=False)
    user_avatar = serializers.ReadOnlyField(source='user.avatar.path')
    user_phone = serializers.ReadOnlyField(source='user.phone_number')
    user_nickname = serializers.ReadOnlyField(source='user.nickname')
    user_register_date = serializers.ReadOnlyField(source='user.register_date')
    region_title = serializers.ReadOnlyField(source='region.title')
    category_title = serializers.ReadOnlyField(source='category.title')
    class Meta:
        model = BaseProduct
        fields = ('title', 'price', 'region', 'add_date', 'slug', 'description','image', 'category', 'views','id',
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

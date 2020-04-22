from .models import Category, Region, BaseProduct, Apartment, Avtomobil, House, Land, Vacancy, Resume
import django_filters

class CategoryFilter(django_filters.FilterSet):
    lft__gte = django_filters.NumberFilter(field_name='lft', lookup_expr='gte')
    rght__lte = django_filters.NumberFilter(field_name='rght', lookup_expr='lte')

    class Meta:
        model = Category
        fields = ['title', 'slug', 'lft', 'rght', 'level', 'tree_id']


class RegionFilter(django_filters.FilterSet):
    lft__gte = django_filters.NumberFilter(field_name='lft', lookup_expr='gte')
    rght__lte = django_filters.NumberFilter(field_name='rght', lookup_expr='lte')

    class Meta:
        model = Region
        fields = ['title', 'slug', 'lft', 'rght', 'level', 'tree_id', 'id']

class BaseProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category_gte = django_filters.NumberFilter(field_name='category__lft', lookup_expr='gte')
    category_lte = django_filters.NumberFilter(field_name='category__rght', lookup_expr='lte')
    region_gte = django_filters.NumberFilter(field_name='region__lft', lookup_expr='gte')
    region_lte = django_filters.NumberFilter(field_name='region__rght', lookup_expr='lte')

    class Meta:
        model = BaseProduct
        order_by_field = 'add_date'
        fields = ['min_price', 'max_price', 'category_gte', 'category_lte', 'region_gte', 'region_lte']


class AvtomobilFilter(BaseProductFilter):
    min_year_issue = django_filters.NumberFilter(field_name='year_issue', lookup_expr='gte')
    max_year_issue = django_filters.NumberFilter(field_name='year_issue', lookup_expr='lte')
    min_mileage = django_filters.NumberFilter(field_name='mileage', lookup_expr='gte')
    max_mileage = django_filters.NumberFilter(field_name='mileage', lookup_expr='lte')


    class Meta:
        model = Avtomobil
        fields = BaseProductFilter.Meta.fields + ['gear_shift', 'body_type', 'engine_type', 'drive_unit', 'condition', 'is_mileage',
                'min_year_issue', 'max_year_issue', 'min_mileage', 'min_mileage']


class ApartmentFilter(BaseProductFilter):
    min_floors_in_house = django_filters.NumberFilter(field_name='floors_in_house', lookup_expr='gte')
    max_floors_in_house = django_filters.NumberFilter(field_name='floors_in_house', lookup_expr='lte')
    min_floor = django_filters.NumberFilter(field_name='floor', lookup_expr='gte')
    max_floor = django_filters.NumberFilter(field_name='floor', lookup_expr='lte')
    min_total_area = django_filters.NumberFilter(field_name='total_area', lookup_expr='gte')
    max_total_area = django_filters.NumberFilter(field_name='total_area', lookup_expr='lte')

    class Meta:
        model = Apartment
        fields = BaseProductFilter.Meta.fields + ['rent_buy', 'number_rooms', 'min_floors_in_house', 'max_floors_in_house',
                'min_floor', 'max_floor', 'min_total_area', 'max_total_area']


class HouseFilter(BaseProductFilter):
    min_house_area = django_filters.NumberFilter(field_name='house_area', lookup_expr='gte')
    max_house_area = django_filters.NumberFilter(field_name='house_area', lookup_expr='lte')
    min_land_area = django_filters.NumberFilter(field_name='land_area', lookup_expr='gte')
    max_land_area = django_filters.NumberFilter(field_name='land_area', lookup_expr='lte')

    class Meta:
        model = House
        fields = BaseProductFilter.Meta.fields + ['min_house_area', 'max_house_area', 'min_land_area', 'max_land_area']


class LandFilter(BaseProductFilter):
    min_land_area = django_filters.NumberFilter(field_name='land_area', lookup_expr='gte')
    max_land_area = django_filters.NumberFilter(field_name='land_area', lookup_expr='lte')

    class Meta:
        model = Land
        fields = BaseProductFilter.Meta.fields + ['min_land_area', 'max_land_area']


class VacancyFilter(BaseProductFilter):

    class Meta:
        model = Vacancy
        fields = BaseProductFilter.Meta.fields + ['schedule', 'work_experience']


class ResumeFilter(VacancyFilter):
    min_age = django_filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_age = django_filters.NumberFilter(field_name='age', lookup_expr='lte')

    class Meta:
        model = Resume
        fields = VacancyFilter.Meta.fields + ['gender', 'min_age', 'max_age']
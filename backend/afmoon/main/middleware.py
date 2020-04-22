from .serializers import HouseSerializer, LandSerializer, VacancySerializer, ResumeSerializer, AvtomobilGetSerializer
from .serializers import CommonProductDetail, AvtomobilSerializer, ApartmentSerializer, AddProductSerializer
from .models import House, Land, Vacancy, Resume, BaseProduct, Avtomobil, Apartment
from .choices import *
from .filters import BaseProductFilter, AvtomobilFilter, ApartmentFilter,HouseFilter, LandFilter, VacancyFilter, ResumeFilter


def get_serializer_class(request):
	category_id = request.data.get('category')
	switcher = {
		'172' : AvtomobilSerializer,
		'169' : ApartmentSerializer,
		'170' : HouseSerializer,
		'171' : LandSerializer,
		'167' : VacancySerializer,
		'168' : ResumeSerializer
	}
	return switcher.get(category_id, AddProductSerializer)


def get_queryset_objects(self):
	category_id = self.request.query_params.get('category')
	if (category_id == '172'):
		self.filterset_class = AvtomobilFilter
		return Avtomobil.objects.filter(is_active=True, is_deleted=False)
	elif (category_id == '169'):
		self.filterset_class = ApartmentFilter
		return Apartment.objects.filter(is_active=True, is_deleted=False)
	elif (category_id == '170'):
		self.filterset_class = HouseFilter
		return House.objects.filter(is_active=True, is_deleted=False)
	elif (category_id == '171'):
		self.filterset_class = LandFilter
		return Land.objects.filter(is_active=True, is_deleted=False)
	elif (category_id == '167'):
		self.filterset_class = VacancyFilter
		return Vacancy.objects.filter(is_active=True, is_deleted=False)
	elif (category_id == '168'):
		self.filterset_class = ResumeFilter
		return Resume.objects.filter(is_active=True, is_deleted=False)
	else:
		self.filterset_class = BaseProductFilter
		return BaseProduct.objects.filter(is_active=True, is_deleted=False).order_by('add_date')

def serializer_get_edit(request,slug):
	baseproduct = BaseProduct.objects.get(slug=slug)
	category = baseproduct.category_id
	if (category == 172 ):
		product = Avtomobil.objects.get(slug=slug)
		if request.user.id == product.user_id:
			data = AvtomobilSerializer(product)
			serializer_data = data.data
			dict_mark_model = get_model_avto(data.data['mark_model'], 0, 1)
			serializer_data['mark'] = dict_mark_model['mark']
			serializer_data['model'] = dict_mark_model['model']
	elif (category == 169 ):
		product = Apartment.objects.get(slug=slug)
		if request.user.id == product.user_id:
			serializer_data = ApartmentSerializer(product)
			serializer_data = serializer_data.data
	elif (category == 170):
		product = House.objects.get(slug=slug)
		if request.user.id == product.user_id:
			serializer_data = HouseSerializer(product)
			serializer_data = serializer_data.data
	elif (category == 171 ):
		product = Land.objects.get(slug=slug)
		if request.user.id == product.user_id:
			serializer_data = LandSerializer(product)
			serializer_data = serializer_data.data
	elif (category == 167 ):
		product = Vacancy.objects.get(slug=slug)
		if request.user.id == product.user_id:
			serializer_data = VacancySerializer(product)
			serializer_data = serializer_data.data
	elif (category == 168 ):
		product = Resume.objects.get(slug=slug)
		if request.user.id == product.user_id:
			serializer_data = ResumeSerializer(product)
			serializer_data = serializer_data.data
	else:
		product = BaseProduct.objects.get(slug=slug)
		if request.user.id == product.user_id:
			serializer_data = CommonProductDetail(product)
			serializer_data = serializer_data.data
	return serializer_data


def serializer_edit(request,slug):
	category = request.data.get('category')
	if (category == str(172) ):
		product = Avtomobil.objects.get(slug=slug)
		serializer_data = AvtomobilSerializer(product, data=request.data)
	elif (category == str(169) ):
		product = Apartment.objects.get(slug=slug)
		serializer_data = ApartmentSerializer(product, data=request.data)
	elif (category == str(170) ):
		product = House.objects.get(slug=slug)
		serializer_data = HouseSerializer(product, data=request.data)
	elif (category == str(171) ):
		product = Land.objects.get(slug=slug)
		serializer_data = LandSerializer(product, data=request.data)
	elif (category == str(167) ):
		product = Vacancy.objects.get(slug=slug)
		serializer_data = VacancySerializer(product, data=request.data)
	elif (category == str(168) ):
		product = Resume.objects.get(slug=slug)
		serializer_data = ResumeSerializer(product, data=request.data)
	else:
		product = BaseProduct.objects.get(slug=slug)
		serializer_data = CommonProductDetail(product, data=request.data)
	return serializer_data




def get_add_detail(request, region, category, slug):
	if (category == 'avtomobili'):
		data = Avtomobil.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = AvtomobilGetSerializer(data)
		additional_data = serializer.data
	elif (category == 'kvartiry'):
		data = Apartment.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = ApartmentSerializer(data)
		additional_data = serializer.data
		if (serializer.data['rent_buy']):
			additional_data['rent_buy'] = 'Продается'
		else:
			additional_data['rent_buy'] = 'Сдается'
		additional_data['number_rooms'] = NUMBER_ROOMS[int(serializer.data['number_rooms']) -1][1]
	elif (category == 'doma-dachi-kottedzhi'):
		data = House.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = HouseSerializer(data)
		additional_data = serializer.data
	elif (category == 'zemelnye-uchastki' ):
		data = Land.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = LandSerializer(data)
		additional_data = serializer.data
	elif (category == 'vakansii'):
		data = Vacancy.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = VacancySerializer(data)
		additional_data = serializer.data
		additional_data['schedule'] = SCHEDULE[int(serializer.data['schedule']) -1][1]
		additional_data['work_experience'] = WORK_EXPERIENCE[int(serializer.data['work_experience']) -1][1]
	elif (category == 'reziume'):
		data = Resume.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = ResumeSerializer(data)
		additional_data = serializer.data
		if (serializer.data['gender']):
			additional_data['gender'] = True
		else:
			additional_data['gender'] = False
		additional_data['schedule'] = SCHEDULE[int(serializer.data['schedule']) -1][1]
		additional_data['work_experience'] = WORK_EXPERIENCE[int(serializer.data['work_experience']) -1][1]
	else:
		data = BaseProduct.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = CommonProductDetail(data)
		additional_data = serializer.data
	additional_data['user_avatar'] = serializer.data['user_avatar'][34:]
	if data.favorite_for.filter(id=request.user.id).exists():
		additional_data['favorite_for'] = True
	else:
		additional_data['favorite_for'] = False
	return additional_data


def ad_filter_by_category(request, region, category):
	if (category.id == 172 ):
		ad_list = Avtomobil.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght, region__lft__gte=region.lft, region__rght__lte=region.rght)
	elif (category.id == 169 ):
		ad_list = Apartment.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght, region__lft__gte=region.lft, region__rght__lte=region.rght)
		if (request.query_params.get('floorsInHouseFrom')):
			ad_list = ad_list.filter(floors_in_house__gte=request.query_params.get('floorsInHouseFrom'))
		if (request.query_params.get('floorsInHouseUp')):
			ad_list = ad_list.filter(floors_in_house__lte=request.query_params.get('floorsInHouseUp'))
		if (request.query_params.get('floorFrom')):
			ad_list = ad_list.filter(floor__gte=request.query_params.get('floorFrom'))
		if (request.query_params.get('floorUp')):
			ad_list = ad_list.filter(floor__lte=request.query_params.get('floorUp'))
		if (request.query_params.get('totalAreaFrom')):
			ad_list = ad_list.filter(total_area__gte=request.query_params.get('totalAreaFrom'))
		if (request.query_params.get('totalAreaUp')):
			ad_list = ad_list.filter(total_area__lte=request.query_params.get('totalAreaUp'))
		if (request.query_params.get('numberRooms')):
			ad_list = ad_list.filter(number_rooms=request.query_params.get('numberRooms'))
	elif (category.id == 170 ):
		ad_list = House.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght, region__lft__gte=region.lft, region__rght__lte=region.rght)
		if (request.query_params.get('houseAreaFrom')):
			ad_list = ad_list.filter(house_area__gte=request.query_params.get('houseAreaFrom'))
		if (request.query_params.get('houseAreaUp')):
			ad_list = ad_list.filter(house_area__lte=request.query_params.get('houseAreaUp'))
		if (request.query_params.get('landAreaFrom')):
			ad_list = ad_list.filter(land_area__gte=request.query_params.get('landAreaFrom'))
		if (request.query_params.get('landAreaUp')):
			ad_list = ad_list.filter(land_area__lte=request.query_params.get('landAreaUp'))
	elif (category.id == 171 ):
		ad_list = Avtomobil.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght, region__lft__gte=region.lft, region__rght__lte=region.rght)
	elif (category.id == 167 ):
		ad_list = Vacancy.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght, region__lft__gte=region.lft, region__rght__lte=region.rght)
		if (request.query_params.get('schedule')):
			ad_list = ad_list.filter(schedule=request.query_params.get('schedule'))
		if (request.query_params.get('workExperience')):
			ad_list = ad_list.filter(work_experience=request.query_params.get('workExperience'))
	elif (category.id == 168 ):
		ad_list = Resume.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght, region__lft__gte=region.lft, region__rght__lte=region.rght)
		if(request.query_params.get('gender')):
			if (request.query_params.get('gender') == 'male'):
				ad_list = ad_list.filter(gender=True)
			elif (request.query_params.get('gender') == 'female'):
				ad_list = ad_list.filter(gender=False)
		if (request.query_params.get('ageFrom')):
			ad_list = ad_list.filter(age__gte=request.query_params.get('ageFrom'))
		if (request.query_params.get('ageUp')):
			ad_list = ad_list.filter(age__lte=request.query_params.get('ageUp'))
		if (request.query_params.get('schedule')):
			ad_list = ad_list.filter(schedule=request.query_params.get('schedule'))
		if (request.query_params.get('workExperience')):
			ad_list = ad_list.filter(work_experience=request.query_params.get('workExperience'))
	else:
		ad_list = BaseProduct.objects.filter(category__lft__gte=category.lft, category__rght__lte=category.rght, region__lft__gte=region.lft, region__rght__lte=region.rght)
	ad_list = ad_list.filter(is_active=True, is_deleted=False)
	return ad_list
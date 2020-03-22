from .serializers import HouseSerializer, LandSerializer, VacancySerializer, ResumeSerializer, SecondSerializer, PersonalsClothesSerializer
from .serializers import PersonalsShoesSerializer, CommonProductDetail, AvtomobilSerializer, ApartmentSerializer, TestProductSerialzier
from .models import House, Land, Vacancy, Resume, Second, Personals_clothes, BaseProduct, Personals_shoes, Avtomobil, Apartment
from .choices import *

def get_model_avto(number,mark=1, model=0):
	for num in range(len(MARK)):
		if ( (MARK[num][1][0][0]-1)<number and (MARK[num][1][len(MARK[num][1]) -1][0] + 1) > number):
			data = { 'mark' : MARK[num][model], 'model' : MARK[num][1][number][mark]}
		return data

def serializer_save(request):
	category = request.data.get('category')
	if (category == str(172) ):
		serializer_data = AvtomobilSerializer(data=request.data)
	elif (category == str(169) ):
		serializer_data = ApartmentSerializer(data=request.data)
	elif (category == str(170) ):
		serializer_data = HouseSerializer(data=request.data)
	elif (category == str(171) ):
		serializer_data = LandSerializer(data=request.data)
	elif (category == str(167) ):
		serializer_data = VacancySerializer(data=request.data)
	elif (category == str(168) ):
		serializer_data = ResumeSerializer(data=request.data)
	elif (category == str(157) or category == str(163) or str(139)):
		serializer_data = PersonalsShoesSerializer(data=request.data)
	elif (category == str(145) or category == str(161)):
		serializer_data = PersonalsClothesSerializer(data=request.data)
	elif (category == str(1134)):
		serializer_data = SecondSerializer(data=request.data)
	else:
		serializer_data = CommonProductDetail(data=request.data)
	return serializer_data

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
	elif (category == 157 or category == 163 or category == 139):
		try:
			product = Personals_shoes.objects.get(slug=slug)
		except Personals_shoes.DoesNotExist:
			product: None
		if request.user.id == product.user_id:
			serializer_data = PersonalsShoesSerializer(product)
			serializer_data = serializer_data.data
	elif (category == 145 or category == 161):
		product = Personals_clothes.objects.get(slug=slug)
		if request.user.id == product.user_id:
			serializer_data = PersonalsClothesSerializer(product)
			serializer_data = serializer_data.data
	elif (category == 1134):
		product = Second.objects.get(slug=slug)
		if request.user.id == product.user_id:
			serializer_data = SecondSerializer(product)
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
	elif (category == str(157) or category == str(163) or category == str(139)):
		product = Personals_shoes.objects.get(slug=slug)
		serializer_data = PersonalsShoesSerializer(product, data=request.data)
	elif (category == str(145) or category == str(161)):
		product = Personals_clothes.objects.get(slug=slug)
		serializer_data = PersonalsClothesSerializer(product, data=request.data)
	elif (category == str(1134)):
		product = Second.objects.get(slug=slug)
		serializer_data = SecondSerializer(product, data=request.data)
	else:
		product = BaseProduct.objects.get(slug=slug)
		serializer_data = CommonProductDetail(product, data=request.data)
	return serializer_data




def get_add_detail(request, region, category, slug):
	if (category == 'avtomobili'):
		data = Avtomobil.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = AvtomobilSerializer(data)
		additional_data = serializer.data
		dict_mark_model = get_model_avto(serializer.data['mark_model'])
		if (serializer.data['condition']):
			additional_data['condition'] = 'Не битый'
		else:
			additional_data['condition'] = 'Битый'
		additional_data['mark'] = dict_mark_model['mark']
		additional_data['model'] = dict_mark_model['model']
		additional_data['gear_shift'] = GEAR_SHIFT[int(serializer.data['gear_shift']) -1][1]
		additional_data['body_type'] = BODY_TYPE[int(serializer.data['body_type']) -1][1]
		additional_data['engine_type'] = ENGINE_TYPE[int(serializer.data['engine_type']) -1][1]
		additional_data['drive_unit'] = DRIVE_UNIT[int(serializer.data['drive_unit']) -1][1]
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
	elif (category == 'detskii-obuv' or category == 'zhenskie-obuvy' or category == 'muzhskoi-obuv'):
		data = Personals_shoes.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = PersonalsShoesSerializer(data)
		additional_data = serializer.data
		additional_data['size'] = SIZE_SHOES[int(serializer.data['schedule']) -1][1]
	elif (category == 'verkhniaia-odezhda' or category == 'zhenskaia-verkhniaia-odezhda'):
		data = Personals_clothes.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = PersonalsClothesSerializer(data)
		additional_data = serializer.data
		additional_data['size'] = SIZE_CLOTHES[int(serializer.data['schedule']) -1][1]
	elif (category == '1132_yetende' ):
		data = Second.objects.get(region__slug=region, category__slug=category, slug=slug)
		serializer = SecondSerializer(data)
		additional_data = serializer.data
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
	return ad_list


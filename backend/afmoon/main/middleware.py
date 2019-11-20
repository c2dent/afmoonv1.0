from .serializers import HouseSerializer, LandSerializer, VacancySerializer, ResumeSerializer, SecondSerializer, PersonalsClothesSerializer
from .serializers import PersonalsShoesSerializer, CommonProductDetail, AvtomobilSerializer, ApartmentSerializer, TestProductSerialzier
from .models import House, Land, Vacancy, Resume, Second, Personals_clothes, BaseProduct, Personals_shoes, Avtomobil, Apartment
from .choices import *

def get_model_avto(number):
	for num in range(len(MARK)):
		if ( (MARK[num][1][0][0]-1)<number and (MARK[num][1][len(MARK[num][1]) -1][0] + 1) > number):
			data = { 'mark' : MARK[num][0], 'model' : MARK[num][1][number][1]}
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
		serializer_data = LandSerialzier(data=request.data)
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

def get_add_detail(region, category, slug):
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
			additional_data['gender'] = 'Муж'
		else:
			additional_data['gender'] = 'Жен'
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
	return additional_data
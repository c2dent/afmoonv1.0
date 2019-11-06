from .serializers import HouseSerializer, LandSerialzier, VacancySerializer, ResumeSerializer, SecondSerializer, PersonalsClothesSerializer
from .serializers import PersonalsShoesSerializer, CommonProductDetail, AvtomobilSerialzier, ApartmentSerializer, TestProductSerialzier


def serializer_save(request):
	category = request.data.get('category')
	if (category == str(172) ):
		serialzier_data = AvtomobilSerialzier(data=request.data)
	elif (category == str(169) ):
		serialzier_data = ApartmentSerializer(data=request.data)
	elif (category == str(170) ):
		serialzier_data = HouseSerializer(data=request.data)
	elif (category == str(171) ):
		serialzier_data = LandSerialzier(data=request.data)
	elif (category == str(167) ):
		serialzier_data = VacancySerializer(data=request.data)
	elif (category == str(168) ):
		serialzier_data = ResumeSerializer(data=request.data)
	elif (category == str(148) or category == str(149) or category == str(150) or category == str(151)):
		serialzier_data = SecondSerializer(data=request.data)
	else:
		serialzier_data = CommonProductDetail(data=request.data)
	return serialzier_data
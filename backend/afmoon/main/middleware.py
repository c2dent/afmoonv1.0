from .serializers import HouseSerializer, LandSerialzier, VacancySerializer, ResumeSerializer, SecondSerializer, PersonalsClothesSerializer
from .serializers import PersonalsShoesSerializer, CommonProductDetail, AvtomobilSerialzier, ApartmentSerializer


def serialzier_save(request):
	request.data['user'] = request.user
	request.data['region'] = request.user.region
	if (request.data.category in (172,) ):
		serialzier_data = AvtomobilSerialzier(data=request.data)
	elif (request.data.category in (169,) ):
		serialzier_data = ApartmentSerializer(data=request.data)
	elif (request.data.category in (170,) ):
		serialzier_data = HouseSerializer(data=request.data)
	elif (request.data.category in (171,) ):
		serialzier_data = LandSerialzier(data=request.data)
	elif (request.data.category in (167,) ):
		serialzier_data = VacancySerializer(data=request.data)
	elif (request.data.category in (168,) ):
		serialzier_data = ResumeSerializer(data=request.data)
	elif (request.data.category in (148,149,150,151) ):
		serialzier_data = SecondSerializer(data=request.data)
	else:
		serialzier_data = CommonProductDetail(data=request.data)
	return serialzier_data
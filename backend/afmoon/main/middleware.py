from .serializers import HouseSerializer, LandSerializer, VacancySerializer, ResumeSerializer
from .serializers import CommonProductDetail, AvtomobilSerializer, ApartmentSerializer
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
	return switcher.get(category_id, CommonProductDetail)


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

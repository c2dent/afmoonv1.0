from django.db.models import F
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from .utilities import generation_token, get_phone, get_otp
from rest_framework.response import Response
from rest_framework import status
from .models import User, BaseProduct, Region, Category
from .serializers import UserSerializer, BaseProductSerializer, RegionSerializer, CategorySerializer
from .serializers import UserAdSerializer, CommonProductDetail, UserFavoriteSerializer, ProductDetailSerializer
from .filters import BaseProductFilter
from .middleware import get_serializer_class, get_queryset_objects
from .choices import *
from .filters import CategoryFilter, RegionFilter
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


@api_view(['POST'])
@permission_classes([AllowAny, ])
def send_sms(request):
	phone_number = request.data.get('phone_number')
	if phone_number:
		data = get_phone(phone_number)
		return Response(data, status=status.HTTP_200_OK)
	return Response({'detail': 'phone number required'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authentification_user(request):
	user_otp = request.data.get('otp')
	phone_number = request.data.get('phone_number')
	otp_key = request.data.get('otp_key')
	if phone_number and user_otp and otp_key:
		data = get_otp(user_otp, otp_key)
		if data['Status'] == "Success":
			if User.objects.filter(phone_number=phone_number).exists():
				user = User.objects.get(phone_number=phone_number)
				user_details = generation_token(user, request)
			else:
				user = User.objects.create_user(phone_number=phone_number)
				user.save()
				user_details = generation_token(user, request)
			return Response(user_details, status=status.HTTP_200_OK)
		else:
			return Response({'detail': 'wrong key'}, status=status.HTTP_400_BAD_REQUEST)
	else:
		return Response({'detail': 'phone number and otp key required field'}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def profile(request):
	serializer = UserSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def user_detail(request, user):
	usr = User.objects.get(id=user)
	serializer = UserSerializer(usr)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def get_user_ad(request):
	serializer = UserAdSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated,])
def get_user_favorites(request):
	serializer = UserFavoriteSerializer(request.user)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def add_remove_favorites(request):
	product = BaseProduct.objects.get(id=request.data.get('product_id'))
	if product.favorite_for.filter(id=request.user.id).exists():
		product.favorite_for.remove(request.user)
	else:
		product.favorite_for.add(request.user)
	return Response(product.id, status=status.HTTP_200_OK)



class CategoryList(generics.ListAPIView):
	permission_classes = [AllowAny,]
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = CategoryFilter


class RegionList(generics.ListAPIView):
	permission_classes = [AllowAny, ]
	queryset = Region.objects.all()
	serializer_class = RegionSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filterset_class = RegionFilter


class ProductList(generics.ListAPIView):
	permission_classes = [AllowAny, ]
	serializer_class = BaseProductSerializer
	filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
	filterset_class = BaseProductFilter
	search_fields = ("title", "description", )
	ordering_fields = ("price",)
	ordering = "-add_date"

	def get_queryset(self):
		if self.request.query_params.get('category') is not None:
			return get_queryset_objects(self)
		else:
			return BaseProduct.objects.all()




class AdDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [AllowAny, ]
	lookup_field = 'slug'
	queryset = BaseProduct.objects.all()
	serializer_class = ProductDetailSerializer

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		BaseProduct.objects.filter(slug=instance.slug).update(views=F('views') + 1)
		serializer = ProductDetailSerializer(instance, context={'request': request})
		return Response(serializer.data)






class AdCreateAPIView(generics.CreateAPIView):
	serializer_class = CommonProductDetail
	def get_serializer_class(self):
		return get_serializer_class(self.request)





@api_view(['PUT'])
@permission_classes([IsAuthenticated,])
def active_ad(request, slug):
	product = BaseProduct.objects.get(slug=slug)
	if product.is_active:
		product.is_active = False
	else:
		product.is_active = True
	product.save()
	serializer = BaseProductSerializer(product)
	return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def get_choices(request):
	available_dicts = {
		"NUMBER_ROOMS": NUMBER_ROOMS,
		"MARK": MARK,
		"GEAR_SHIFT": GEAR_SHIFT,
		"BODY_TYPE": BODY_TYPE,
		"ENGINE_TYPE": ENGINE_TYPE,
		"DRIVE_UNIT": DRIVE_UNIT,
		"SCHEDULE": SCHEDULE,
		"WORK_EXPERIENCE": WORK_EXPERIENCE
	}
	choices = request.query_params.get('choices')
	if choices is not None and choices in available_dicts:
		result_list = []
		chosen_dict = available_dicts[choices]
		result_list = chosen_dict
		return Response(result_list, status=status.HTTP_200_OK)
	else:
		return Response({'Error': 'Empty or invalid choice given'}, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
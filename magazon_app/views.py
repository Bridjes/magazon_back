from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt import tokens, views
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from .models import *

####### "ЛЕГКОВЫЕ АВТО" #######
# вывод списка автомобилей
class CarRetrieveView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarRetrieveSerializer

# создать новый автомобиль
class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
    permission_classes = (IsAuthenticated, )

# обновить указанный автомобиль
class CarUpdateView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarUpdateSerializer
    permission_classes = (IsAuthenticated, )

####### АВТОРИЗАЦИЯ #######
# регистрация пользователей
class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer

# login
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# logout
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = tokens.RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=204)
        except Exception as e:
            return Response(status=400)

####### КАСТОМИЗАЦИЯ JWT-ТОКЕНОВ #######
class MyTokenObtainPairView(views.TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
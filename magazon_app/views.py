from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.permissions import *
from .serializers import *
from .models import *

####### "ЛЕГКОВЫЕ АВТО" #######
class CarRetrieveView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarRetrieveSerializer

class CarCreate(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarRetrieveSerializer
    # permission_classes = (IsAuthenticated, )

####### Регистрация пользователей #######
class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
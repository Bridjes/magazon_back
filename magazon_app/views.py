from rest_framework import viewsets, generics
from rest_framework.permissions import *

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
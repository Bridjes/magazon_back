from rest_framework import viewsets, generics
from rest_framework.permissions import *

from .serializers import *
from .models import *

###### ЛЕГКОВЫЕ АВТО ######
class CarRetrieveView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarRetrieveSerializer
class CarCreateView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarCreateSerializer
    permission_classes = (IsAuthenticated, )
class CarUpdateView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### ГРУЗОВИКИ И АВТОБУСЫ ######
class TruckRetrieveView(generics.ListAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckRetrieveSerializer
class TruckCreateView(generics.CreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckCreateSerializer
    permission_classes = (IsAuthenticated, )
class TruckUpdateView(generics.UpdateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### МОТОЦИКЛЫ ######
class MotorbikeRetrieveView(generics.ListAPIView):
    queryset = Motorbike.objects.all()
    serializer_class = MotorbikeRetrieveSerializer
class MotorbikeCreateView(generics.CreateAPIView):
    queryset = Motorbike.objects.all()
    serializer_class = MotorbikeCreateSerializer
    permission_classes = (IsAuthenticated, )
class MotorbikeUpdateView(generics.UpdateAPIView):
    queryset = Motorbike.objects.all()
    serializer_class = MotorbikeUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### КВАРТИРЫ ######
class ApartmentRetrieveView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentRetrieveSerializer
class ApartmentCreateView(generics.CreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentCreateSerializer
    permission_classes = (IsAuthenticated, )
class ApartmentUpdateView(generics.UpdateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### ДОМА, ДАЧИ, КОТТЕДЖИ ######
class CottageRetrieveView(generics.ListAPIView):
    queryset = Cottage.objects.all()
    serializer_class = CottageRetrieveSerializer
class CottageCreateView(generics.CreateAPIView):
    queryset = Cottage.objects.all()
    serializer_class = CottageCreateSerializer
    permission_classes = (IsAuthenticated, )
class CottageUpdateView(generics.UpdateAPIView):
    queryset = Cottage.objects.all()
    serializer_class = CottageUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### ГАРАЖИ И СТОЯНКИ ######
class GarageRetrieveView(generics.ListAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageRetrieveSerializer
class GarageCreateView(generics.CreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageCreateSerializer
    permission_classes = (IsAuthenticated, )
class GarageUpdateView(generics.UpdateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### АУДИОТЕХНИКА ######
class AudioRetrieveView(generics.ListAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioRetrieveSerializer
class AudioCreateView(generics.CreateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioCreateSerializer
    permission_classes = (IsAuthenticated, )
class AudioUpdateView(generics.UpdateAPIView):
    queryset = Audio.objects.all()
    serializer_class = AudioUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### НАУШНИКИ ######
class HeadphonesRetrieveView(generics.ListAPIView):
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesRetrieveSerializer
class HeadphonesCreateView(generics.CreateAPIView):
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesCreateSerializer
    permission_classes = (IsAuthenticated, )
class HeadphonesUpdateView(generics.UpdateAPIView):
    queryset = Headphones.objects.all()
    serializer_class = HeadphonesUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### ТВ И ВИДЕОТЕХНИКА ######
class VideoEquipmentRetrieveView(generics.ListAPIView):
    queryset = VideoEquipment.objects.all()
    serializer_class = VideoEquipmentRetrieveSerializer
class VideoEquipmentCreateView(generics.CreateAPIView):
    queryset = VideoEquipment.objects.all()
    serializer_class = VideoEquipmentCreateSerializer
    permission_classes = (IsAuthenticated, )
class VideoEquipmentUpdateView(generics.UpdateAPIView):
    queryset = VideoEquipment.objects.all()
    serializer_class = VideoEquipmentUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### БАНКЕТКИ И ПУФИКИ ######
class OttomansRetrieveView(generics.ListAPIView):
    queryset = Ottomans.objects.all()
    serializer_class = OttomansRetrieveSerializer
class OttomansCreateView(generics.CreateAPIView):
    queryset = Ottomans.objects.all()
    serializer_class = OttomansCreateSerializer
    permission_classes = (IsAuthenticated, )
class OttomansUpdateView(generics.UpdateAPIView):
    queryset = Ottomans.objects.all()
    serializer_class = OttomansUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### ВЕШАЛКИ, ПРИХОЖИЕ ######
class HangerRetrieveView(generics.ListAPIView):
    queryset = Hanger.objects.all()
    serializer_class = HangerRetrieveSerializer
class HangerCreateView(generics.CreateAPIView):
    queryset = Hanger.objects.all()
    serializer_class = HangerCreateSerializer
    permission_classes = (IsAuthenticated, )
class HangerUpdateView(generics.UpdateAPIView):
    queryset = Hanger.objects.all()
    serializer_class = HangerUpdateSerializer
    permission_classes = (IsAuthenticated, )

###### КОМОДЫ ######
class DresserRetrieveView(generics.ListAPIView):
    queryset = Dresser.objects.all()
    serializer_class = DresserRetrieveSerializer
class DresserCreateView(generics.CreateAPIView):
    queryset = Dresser.objects.all()
    serializer_class = DresserCreateSerializer
    permission_classes = (IsAuthenticated, )
class DresserUpdateView(generics.UpdateAPIView):
    queryset = Dresser.objects.all()
    serializer_class = DresserUpdateSerializer
    permission_classes = (IsAuthenticated, )

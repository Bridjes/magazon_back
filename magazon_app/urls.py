from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
from .views import *

urlpatterns = [
    ###### ЛЕГКОВЫЕ АВТО ######
    path('v1/cars/retrieve/', CarRetrieveView.as_view()),
    path('v1/cars/create/', CarCreateView.as_view()),
    path('v1/cars/update/<int:pk>', CarUpdateView.as_view()),

    ###### ГРУЗОВИКИ И АВТОБУСЫ ######
    path('v1/truck/retrieve/', TruckRetrieveView.as_view()),
    path('v1/truck/create/', TruckCreateView.as_view()),
    path('v1/truck/update/<int:pk>', TruckUpdateView.as_view()),

    ###### МОТОЦИКЛЫ ######
    path('v1/motorbike/retrieve/', MotorbikeRetrieveView.as_view()),
    path('v1/motorbike/create/', MotorbikeCreateView.as_view()),
    path('v1/motorbike/update/<int:pk>', MotorbikeUpdateView.as_view()),

    ###### КВАРТИРЫ ######
    path('v1/apartment/retrieve/', ApartmentRetrieveView.as_view()),
    path('v1/apartment/create/', ApartmentCreateView.as_view()),
    path('v1/apartment/update/<int:pk>', ApartmentUpdateView.as_view()),

    ###### ДОМА, ДАЧИ, КОТТЕДЖИ ######
    path('v1/cottage/retrieve/', CottageRetrieveView.as_view()),
    path('v1/cottage/create/', CottageCreateView.as_view()),
    path('v1/cottage/update/<int:pk>', CottageUpdateView.as_view()),

    ###### ГАРАЖИ И СТОЯНКИ ######
    path('v1/garage/retrieve/', GarageRetrieveView.as_view()),
    path('v1/garage/create/', GarageCreateView.as_view()),
    path('v1/garage/update/<int:pk>', GarageUpdateView.as_view()),

    ###### АУДИОТЕХНИКА ######
    path('v1/audio/retrieve/', AudioRetrieveView.as_view()),
    path('v1/audio/create/', AudioCreateView.as_view()),
    path('v1/audio/update/<int:pk>', AudioUpdateView.as_view()),

    ###### НАУШНИКИ ######
    path('v1/headphones/retrieve/', HeadphonesRetrieveView.as_view()),
    path('v1/headphones/create/', HeadphonesCreateView.as_view()),
    path('v1/headphones/update/<int:pk>', HeadphonesUpdateView.as_view()),

    ###### ТВ И ВИДЕОТЕХНИКА ######
    path('v1/video_equipment/retrieve/', VideoEquipmentRetrieveView.as_view()),
    path('v1/video_equipment/create/', VideoEquipmentCreateView.as_view()),
    path('v1/video_equipment/update/<int:pk>', VideoEquipmentUpdateView.as_view()),

    ###### БАНКЕТКИ И ПУФИКИ ######
    path('v1/ottomans/retrieve/', OttomansRetrieveView.as_view()),
    path('v1/ottomans/create/', OttomansCreateView.as_view()),
    path('v1/ottomans/update/<int:pk>', OttomansUpdateView.as_view()),

    ###### ВЕШАЛКИ, ПРИХОЖИЕ ######
    path('v1/hanger/retrieve/', HangerRetrieveView.as_view()),
    path('v1/hanger/create/', HangerCreateView.as_view()),
    path('v1/hanger/update/<int:pk>', HangerUpdateView.as_view()),

    ###### КОМОДЫ ######
    path('v1/dresser/retrieve/', DresserRetrieveView.as_view()),
    path('v1/dresser/create/', DresserCreateView.as_view()),
    path('v1/dresser/update/<int:pk>', DresserUpdateView.as_view()),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView
from .views import *

urlpatterns = [
    path('v1/cars/retrieve/', CarRetrieveView.as_view()),
    path('v1/cars/create/', CarCreateView.as_view()),
    path('v1/cars/update/<int:pk>', CarUpdateView.as_view()),
]
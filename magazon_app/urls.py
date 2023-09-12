from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *

urlpatterns = [
    path('v1/cars/retrieve/', CarRetrieveView.as_view()),
    path('v1/cars/create/', CarCreateView.as_view()),
    path('v1/cars/update/<int:pk>', CarUpdateView.as_view()),

    path('v1/user/register/', CreateUserView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
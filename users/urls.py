from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenBlacklistView
from .views import *

urlpatterns = [
    path('v1/user/register/', RegisterView.as_view()),
    path('v1/user/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/user/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/user/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/user/logout/', LogoutView.as_view(), name='logout'),
    path('v1/user/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
]
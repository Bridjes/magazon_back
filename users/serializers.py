from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import User
from rest_framework import serializers

####### АВТОРИЗАЦИЯ #######

# register
class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'token', 'username')

    def get_token(self, obj):
        access_token = AccessToken.for_user(obj)
        refresh_token = RefreshToken.for_user(obj)
        return {
            'access': str(access_token),
            'refresh': str(refresh_token),
        }

    # проверка на уникальность email
    def validate(self, data):
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email уже зарегистрирован')
        return data

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data.pop('email', None)
        instance.email = email or instance.email
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

# login
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        return data

######### КАСТОМИЗАЦИЯ JWT-ТОКЕНОВ #########
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
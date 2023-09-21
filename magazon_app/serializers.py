from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

###### ЛЕГКОВЫЕ АВТО ######

# вывод списка автомобилей
class CarRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

# запись нового автомобиля в БД
class CarCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class CarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = [
            'id_service',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

    def update(self, instance, validated_data):
        # убираем ключи со значениями None из словаря
        for key, value in list(validated_data.items()):
            if value is None:
                del validated_data[key]

        instance.title = validated_data.get('title', instance.title)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.body_type = validated_data.get('body_type', instance.body_type)
        instance.color = validated_data.get('color', instance.color)
        instance.engine_type = validated_data.get('engine_type', instance.engine_type)
        instance.drive_unit = validated_data.get('drive_unit', instance.drive_unit)
        instance.transmission = validated_data.get('transmission', instance.transmission)
        instance.engine_volume = validated_data.get('engine_volume', instance.engine_volume)
        instance.year = validated_data.get('year', instance.year)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.air_conditioner = validated_data.get('air_conditioner', instance.air_conditioner)
        instance.seat_heating = validated_data.get('seat_heating', instance.seat_heating)
        instance.abs_esp_asr = validated_data.get('abs_esp_asr', instance.abs_esp_asr)
        instance.regular_navigation = validated_data.get('regular_navigation', instance.regular_navigation)
        instance.alloy_wheels = validated_data.get('alloy_wheels', instance.alloy_wheels)
        instance.parctronic_camera = validated_data.get('parctronic_camera', instance.parctronic_camera)
        instance.sunroof = validated_data.get('sunroof', instance.sunroof)
        instance.theft_protection = validated_data.get('theft_protection', instance.theft_protection)
        instance.xenon = validated_data.get('xenon', instance.xenon)
        instance.cruise_control = validated_data.get('cruise_control', instance.cruise_control)
        instance.aux_usb_bluetooth = validated_data.get('aux_usb_bluetooth', instance.aux_usb_bluetooth)
        instance.state = validated_data.get('state', instance.state)
        instance.vin = validated_data.get('vin', instance.vin)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.leasing = validated_data.get('leasing', instance.leasing)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

###### ЛЕГКОВЫЕ АВТО ######

class CarRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

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

###### ГРУЗОВИКИ И АВТОБУСЫ ######

class TruckRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'

class TruckCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя
    class Meta:
        model = Truck
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class TruckUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.type = validated_data.get('type', instance.type)
        instance.load_capacity = validated_data.get('load_capacity', instance.load_capacity)
        instance.transmission = validated_data.get('transmission', instance.transmission)
        instance.year = validated_data.get('year', instance.year)
        instance.mileage = validated_data.get('mileage', instance.mileage)
        instance.state = validated_data.get('state', instance.state)

        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.leasing = validated_data.get('leasing', instance.leasing)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### МОТОЦИКЛЫ ######
class MotorbikeRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorbike
        fields = '__all__'

class MotorbikeCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Motorbike
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class MotorbikeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorbike
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.type = validated_data.get('type', instance.type)
        instance.truck_dive_unit = validated_data.get('truck_dive_unit', instance.truck_dive_unit)
        instance.number_cycles = validated_data.get('number_cycles', instance.number_cycles)
        instance.number_cylinders = validated_data.get('number_cylinders', instance.number_cylinders)
        instance.number_volume = validated_data.get('number_volume', instance.number_volume)
        instance.year = validated_data.get('year', instance.year)

        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.leasing = validated_data.get('leasing', instance.leasing)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### КВАРТИРЫ ######
class ApartmentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class ApartmentCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Apartment
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class ApartmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.deal_type = validated_data.get('deal_type', instance.deal_type)
        instance.address = validated_data.get('address', instance.address)
        instance.rooms = validated_data.get('rooms', instance.rooms)
        instance.layout = validated_data.get('layout', instance.layout)
        instance.floors = validated_data.get('floors', instance.floors)
        instance.ceiling_height = validated_data.get('ceiling_height', instance.ceiling_height)
        instance.wall_material = validated_data.get('wall_material', instance.wall_material)
        instance.salesman = validated_data.get('salesman', instance.salesman)

        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance


###### ДОМА, ДАЧИ, КОТТЕДЖИ ######
class CottageRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cottage
        fields = '__all__'

class CottageCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Cottage
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class CottageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cottage
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.deal_type = validated_data.get('deal_type', instance.deal_type)
        instance.address = validated_data.get('address', instance.address)
        instance.salesman = validated_data.get('salesman', instance.salesman)

        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### ГАРАЖИ И СТОЯНКИ ######
class GarageRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'

class GarageCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Garage
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class GarageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.deal_type = validated_data.get('deal_type', instance.deal_type)
        instance.address = validated_data.get('address', instance.address)
        instance.salesman = validated_data.get('salesman', instance.salesman)

        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### АУДИОТЕХНИКА ######
class AudioRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'

class AudioCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Audio
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class AudioUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.type = validated_data.get('type', instance.type)
        instance.state = validated_data.get('state', instance.state)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### НАУШНИКИ ######
class HeadphonesRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headphones
        fields = '__all__'

class HeadphonesCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Headphones
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class HeadphonesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headphones
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.type = validated_data.get('type', instance.type)
        instance.wireless = validated_data.get('wireless', instance.wireless)
        instance.brand = validated_data.get('brand', instance.brand)
        instance.connector = validated_data.get('connector', instance.connector)
        instance.purpose = validated_data.get('purpose', instance.purpose)
        instance.fastening = validated_data.get('fastening', instance.fastening)
        instance.noise_reduction = validated_data.get('noise_reduction', instance.noise_reduction)
        instance.surround_sound = validated_data.get('surround_sound', instance.surround_sound)
        instance.folding = validated_data.get('folding', instance.folding)
        instance.volume_control = validated_data.get('volume_control', instance.volume_control)
        instance.protection = validated_data.get('protection', instance.protection)
        instance.microphone = validated_data.get('microphone', instance.microphone)
        instance.NFC = validated_data.get('NFC', instance.NFC)
        instance.state = validated_data.get('state', instance.state)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### ТВ И ВИДЕОТЕХНИКА ######
class VideoEquipmentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoEquipment
        fields = '__all__'

class VideoEquipmentCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = VideoEquipment
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class VideoEquipmentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoEquipment
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.type = validated_data.get('type', instance.type)
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.state = validated_data.get('state', instance.state)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### БАНКЕТКИ И ПУФИКИ ######
class OttomansRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ottomans
        fields = '__all__'

class OttomansCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Ottomans
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class OttomansUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ottomans
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.type = validated_data.get('type', instance.type)
        instance.box = validated_data.get('box', instance.box)
        instance.living_room = validated_data.get('living_room', instance.living_room)
        instance.bedroom = validated_data.get('bedroom', instance.bedroom)
        instance.kitchen = validated_data.get('kitchen', instance.kitchen)
        instance.bathroom = validated_data.get('bathroom', instance.bathroom)
        instance.hallway = validated_data.get('hallway', instance.hallway)
        instance.office = validated_data.get('office', instance.office)
        instance.state = validated_data.get('state', instance.state)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### ВЕШАЛКИ, ПРИХОЖИЕ ######
class HangerRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hanger
        fields = '__all__'

class HangerCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Hanger
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class HangerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hanger
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.type = validated_data.get('type', instance.type)
        instance.fastening = validated_data.get('fastening', instance.fastening)
        instance.living_room = validated_data.get('living_room', instance.living_room)
        instance.bedroom = validated_data.get('bedroom', instance.bedroom)
        instance.kitchen = validated_data.get('kitchen', instance.kitchen)
        instance.bathroom = validated_data.get('bathroom', instance.bathroom)
        instance.hallway = validated_data.get('hallway', instance.hallway)
        instance.office = validated_data.get('office', instance.office)
        instance.state = validated_data.get('state', instance.state)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

###### КОМОДЫ ######
class DresserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dresser
        fields = '__all__'

class DresserCreateSerializer(serializers.ModelSerializer):
    user_create = serializers.HiddenField(
        default=serializers.CurrentUserDefault())  # поле user должно быть скрытым и автоматически заполняться данными текущего пользователя

    class Meta:
        model = Dresser
        fields = '__all__'
        read_only_fields = [
            'id',
            'category',
            'subcategory',
            'user_create',
            'grade',
        ]

class DresserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dresser
        fields = '__all__'
        read_only_fields = [
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
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.living_room = validated_data.get('living_room', instance.living_room)
        instance.bedroom = validated_data.get('bedroom', instance.bedroom)
        instance.kitchen = validated_data.get('kitchen', instance.kitchen)
        instance.bathroom = validated_data.get('bathroom', instance.bathroom)
        instance.hallway = validated_data.get('hallway', instance.hallway)
        instance.office = validated_data.get('office', instance.office)
        instance.state = validated_data.get('state', instance.state)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.exchange = validated_data.get('exchange', instance.exchange)
        instance.installment_plan = validated_data.get('installment_plan', instance.installment_plan)
        instance.city = validated_data.get('city', instance.city)

        instance.user_create = User.objects.latest('pk')
        instance.save()
        return instance

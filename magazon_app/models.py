from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .models_lists import *

########## АВТО И ТРАНСПОРТ ###########

# ___________легковые авто_____________
# марки легковых авто
class CarBrand(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Марка")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Марку"
        verbose_name_plural = "Легковые авто - Марки"

# Модели легковых авто
class CarModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Модель")
    car_brand = models.ForeignKey(CarBrand, verbose_name="Марка", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Модель"
        verbose_name_plural = "Легковые авто - Модели"

# легковые авто
class Car(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Авто и транспорт")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Легковые авто")
    carBrand = models.ForeignKey(CarBrand, on_delete=models.PROTECT, verbose_name="Марка")
    carModel = models.ForeignKey(CarModel, on_delete=models.PROTECT, verbose_name="Модель")
    bodyType = models.CharField(max_length=200, verbose_name="Тип кузова", choices=CAR_BODY_TYPE)
    carColor = models.CharField(max_length=200, verbose_name="Цвет", choices=CAR_COLOR)
    engineType = models.CharField(max_length=200, verbose_name="Тип двигателя", choices=CAR_ENGIN_TYPE)
    driveUnit = models.CharField(max_length=200, verbose_name="Привод", choices=CAR_DRIVE_UNIT)
    transmission = models.CharField(max_length=200, verbose_name="Коробка передач", choices=CAR_TRANSMISSION)
    engineVolume = models.CharField(max_length=200, verbose_name="Объём двигателя", choices=CAR_ENGINE_VOLUME)
    year = models.CharField(max_length=200, verbose_name="Год", choices=CAR_YEAR)
    mileage = models.IntegerField(verbose_name="Пробег, км")
    air_conditioner = models.BooleanField(verbose_name="Кондиционер / климат-контроль")
    seat_heating = models.BooleanField(verbose_name="Обогрев сидений")
    abs_esp_asr = models.BooleanField(verbose_name="ABS / ESP / ASR")
    regular_navigation = models.BooleanField(verbose_name="Regular navigation")
    alloy_wheels = models.BooleanField(verbose_name="Легкосплавные диски")
    parctronic_camera= models.BooleanField(verbose_name="Парктроник / камера")
    sunroof = models.BooleanField(verbose_name="Люк / панорамная крыша")
    theft_protection = models.BooleanField(verbose_name="Защита от угона")
    xenon = models.BooleanField(verbose_name="Ксенон / биксенон")
    cruise_control= models.BooleanField(verbose_name="Круиз-контроль")
    aux_usb_bluetooth = models.BooleanField(verbose_name="AUX / USB / Bluetooth")
    state = models.CharField(max_length=200, verbose_name="Состояние", choices=CAR_STATE)
    vin = models.CharField(max_length=150, unique=True, verbose_name="Номер VIN")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    leasing = models.BooleanField(verbose_name="Лизинг от продавца")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Легковой автомобиль"
        verbose_name_plural = "Легковые авто"

# ___________грузовые авто_____________
# марки грузовых авто
class TruckBrand(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Марка")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Марку"
        verbose_name_plural = "Грузовые авто - Марки"

# грузовые авто
class Truck(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Авто и транспорт")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Грузовики и автобусы")
    truck_brand = models.ForeignKey(TruckBrand, on_delete=models.PROTECT, verbose_name="Марка")
    truck_type = models.CharField(max_length=200, verbose_name="Тип грузовика", choices=TRUCK_TYPE)
    truck_load_capacity = models.CharField(max_length=200, verbose_name="Грузоподъемность", choices=TRUCK_LOAD_CAPACITY)
    truck_transmission = models.CharField(max_length=200, verbose_name="Коробка передач", choices=TRUCK_TRANSMISSION)
    year = models.CharField(max_length=200, verbose_name="Год", choices=CAR_YEAR)
    mileage = models.IntegerField(verbose_name="Пробег, км")
    state = models.CharField(max_length=200, verbose_name="Состояние", choices=CAR_STATE)
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    leasing = models.BooleanField(verbose_name="Лизинг от продавца")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Грузовой автомобиль"
        verbose_name_plural = "Грузовые авто"

# ___________ мототехника _____________

# марка мотоцикла
class MotorbikeBrand(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Марка")

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Марку"
        verbose_name_plural = "Мотоциклы - Марки"

# мотоциклы
class Motorbike(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Авто и транспорт")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Мотоциклы")
    brand = models.ForeignKey(MotorbikeBrand, on_delete=models.PROTECT, verbose_name="Марка")
    type = models.CharField(max_length=50, verbose_name="Тип мотоцикла", choices=MOTOBIKE_TYPE)
    truck_dive_unit = models.CharField(max_length=50, verbose_name="Привод", choices=MOTOBILE_DRIVE_UNIT)
    number_cycles = models.CharField(max_length=50, verbose_name="Количество тактов", choices=MOTOBIKE_NUMBER_CYCLES)
    number_cylinders = models.CharField(max_length=50, verbose_name="Количество цилиндров", choices=MOTOBIKE_NUMBER_CYLINDERS)
    number_volume = models.CharField(max_length=50, verbose_name="Объём, см³", choices=MOTOVIKE_VOLUME)
    year = models.CharField(max_length=200, verbose_name="Год", choices=CAR_YEAR)
    mileage = models.IntegerField(verbose_name="Пробег, км")
    state = models.CharField(max_length=200, verbose_name="Состояние", choices=CAR_STATE)
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    leasing = models.BooleanField(verbose_name="Лизинг от продавца")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Мотоцикл"
        verbose_name_plural = "Мотоциклы"


############ НЕДВИЖИМОСТЬ ############

# ___________ Квартиры _______________

# квартиры - тип сделки
class ApartmentDealType(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Тип сделки")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Тип сделки"
        verbose_name_plural = "Квартиры - Тип сделки"

# квартиры - количество комнат
class ApartmentRooms(models.Model):
    value = models.IntegerField(unique=True, verbose_name="Количество комнат")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Количество комнат"
        verbose_name_plural = "Квартиры - Количество комнат"

# квартиры - вид планировки
class ApartmentLayout(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Вид планировки")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Вид планировки"
        verbose_name_plural = "Квартиры - Виды планировок"

# квартиры - количество комнат
class ApartmentFloors(models.Model):
    value = models.IntegerField(unique=True, verbose_name="Этаж")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Этажи"
        verbose_name_plural = "Квартиры - Этажи"

# квартиры - высота потолков
class ApartmentCeilingHeight(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Высота потолков")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Высоту потолков"
        verbose_name_plural = "Квартиры - Высоты потолков"

# квартиры - материал стен
class ApartmentWallMaterial(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Материал стен")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Материал стен"
        verbose_name_plural = "Квартиры - Материалы стен"

# квартиры - продавец
class ApartmentSalesman(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Продавец")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Продавца"
        verbose_name_plural = "Квартиры - Продавцы"

# квартиры
class Apartment(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Недвижимость")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Квартиры")
    deal_type = models.ForeignKey(ApartmentDealType, on_delete=models.SET_NULL, verbose_name="Тип сделки", null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    rooms = models.ForeignKey(ApartmentRooms, on_delete=models.PROTECT, verbose_name="Количество комнат")
    layout = models.ForeignKey(ApartmentLayout, on_delete=models.PROTECT, verbose_name="Вид планировки")
    floors = models.ForeignKey(ApartmentFloors, on_delete=models.PROTECT, verbose_name="Этажность дома")
    ceiling_height = models.ForeignKey(ApartmentCeilingHeight, on_delete=models.PROTECT, verbose_name="Высота потолков")
    wall_material = models.ForeignKey(ApartmentWallMaterial, on_delete=models.PROTECT, verbose_name="Материал стен")
    salesman = models.ForeignKey(ApartmentSalesman, on_delete=models.PROTECT, verbose_name="Продавец")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Квартиру"
        verbose_name_plural = "Квартиры"

# ___________ Дома, дачи, коттеджи ____________

class Cottage(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Недвижимость")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Дома, дачи, коттеджи")
    deal_type = models.ForeignKey(ApartmentDealType, on_delete=models.SET_NULL, verbose_name="Тип сделки", null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    salesman = models.ForeignKey(ApartmentSalesman, on_delete=models.PROTECT, verbose_name="Продавец")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома, квартиры, дачи"

# ___________ Гаражи и стоянки ______________
class Garage(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Недвижимость")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Гаражи и стоянки")
    deal_type = models.ForeignKey(ApartmentDealType, on_delete=models.SET_NULL, verbose_name="Тип сделки", null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    salesman = models.ForeignKey(ApartmentSalesman, on_delete=models.PROTECT, verbose_name="Продавец")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Гараж/стоянку"
        verbose_name_plural = "Гаражи и стоянки"


############ ЭЛЕКТРОНИКА ############

# ___________Аудиотехника____________

# тип аудиотехники
class AudioType(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Тип")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Аудиотехника - Типы"

# состояние аудиотехники
class AudioState(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Состояние")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Состояние"
        verbose_name_plural = "Аудиотехника - Состояние"

# аудиотехника
class Audio(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Электроника")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Аудиотехника")
    type = models.ForeignKey(AudioType, on_delete=models.PROTECT, verbose_name="Тип")
    state = models.ForeignKey(AudioState, on_delete=models.PROTECT, verbose_name="Состояние")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Аудиотехнику"
        verbose_name_plural = "Аудиотехника"

# _______ Наушники ___________

# тип наушников
class HeadphonesType(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Тип")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Наушники - Типы"

# производитель наушников
class HeadphonesManufacturer(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Производитель")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Производителя"
        verbose_name_plural = "Наушники - Производители"

# тип разъема наушников
class HeadphonesConnector(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Тип разъёма")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Тип разъёма"
        verbose_name_plural = "Наушники - Типы разъёмов"

# назначение наушников
class HeadphonesPurpose(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Назначение")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Назначение"
        verbose_name_plural = "Наушники - Назначения"

# крепление наушников
class HeadphonesFastening(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Крепление")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Крепление"
        verbose_name_plural = "Наушники - Крепления"

# наушники
class Headphones(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Электроника")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Наушники")
    type = models.ForeignKey(HeadphonesType, on_delete=models.PROTECT, verbose_name="Тип")
    wireless = models.BooleanField(verbose_name="Беспроводные")
    manufacturer = models.ForeignKey(HeadphonesManufacturer, on_delete=models.PROTECT, verbose_name="Производитель")
    connector = models.ForeignKey(HeadphonesConnector, on_delete=models.PROTECT, verbose_name="Тип разъёма")
    purpose = models.ForeignKey(HeadphonesPurpose, on_delete=models.PROTECT, verbose_name="Назначение")
    fastening = models.ForeignKey(HeadphonesFastening, on_delete=models.PROTECT, verbose_name="Крепление")
    noise_reduction = models.BooleanField(verbose_name="Активное шумоподавление")
    surround_sound = models.BooleanField(verbose_name="Объёмное звучание")
    folding = models.BooleanField(verbose_name="Возможность складывания")
    volume_control = models.BooleanField(verbose_name="Регулировка громкости")
    protection = models.BooleanField(verbose_name="Пыле- и влагозащита")
    microphone = models.BooleanField(verbose_name="Микрофон")
    NFC = models.BooleanField(verbose_name="NFC")
    state = models.ForeignKey(AudioState, on_delete=models.PROTECT, verbose_name="Состояние")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Наушники"
        verbose_name_plural = "Наушники"

# ________ ТВ и видеотехника __________

# тип видеотехники
class VideoEquipmentType(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Тип")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "ТВ и видеотехника - Типы"

# производитель видеотехники
class VideoEquipmentManufacturer(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Производитель")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Производителя"
        verbose_name_plural = "ТВ и видеотехника - Производители"

# ТВ и видеотехника
class VideoEquipment(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Электроника")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="ТВ и видеотехника")
    type = models.ForeignKey(VideoEquipmentType, on_delete=models.PROTECT, verbose_name="Тип")
    manufacturer = models.ForeignKey(VideoEquipmentManufacturer, on_delete=models.PROTECT, verbose_name="Производитель")
    state = models.ForeignKey(AudioState, on_delete=models.PROTECT, verbose_name="Состояние")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "ТВ/видеотехнику"
        verbose_name_plural = "ТВ и видеотехника"

############## МЕБЕЛЬ ##############

# _______ банкетки и пуфики ________

# тип банкеток и пуфиков
class OttomansType(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Тип")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Банкетки и пуфики - Типы"

# банкетки и пуфики
class Ottomans(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Мебель")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Банкетки и пуфики")
    type = models.ForeignKey(OttomansType, on_delete=models.PROTECT, verbose_name="Тип")
    box = models.BooleanField(verbose_name="С ящиком")
    living_room = models.BooleanField(verbose_name="Для гостиной")
    bedroom = models.BooleanField(verbose_name="Для спальни")
    kitchen = models.BooleanField(verbose_name="Для кухни")
    bathroom = models.BooleanField(verbose_name="Для ванной комнаты")
    hallway = models.BooleanField(verbose_name="Для прихожей")
    office = models.BooleanField(verbose_name="Для офиса")
    state = models.ForeignKey(AudioState, on_delete=models.PROTECT, verbose_name="Состояние")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Банкетку/пуфик"
        verbose_name_plural = "Банкетки и пуфики"

# _______ Вешалки, прихожие ________

# тип вешалки, прихожей
class HangerType(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Тип")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Вешалки, прихожие - Типы"

# способ крепления
class HangerFastening(models.Model):
    value = models.CharField(max_length=150, unique=True, verbose_name="Способ крепления")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Способ крепления"
        verbose_name_plural = "Вешалки, прихожие - Способы крепления"

# вешалки, прихожие
class Hanger(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Мебель")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Вешалки, прихожие")
    type = models.ForeignKey(HangerType, on_delete=models.PROTECT, verbose_name="Тип")
    fastening = models.ForeignKey(HangerFastening, on_delete=models.PROTECT, verbose_name="Способ крепления")
    living_room = models.BooleanField(verbose_name="Для гостиной")
    bedroom = models.BooleanField(verbose_name="Для спальни")
    kitchen = models.BooleanField(verbose_name="Для кухни")
    bathroom = models.BooleanField(verbose_name="Для ванной комнаты")
    hallway = models.BooleanField(verbose_name="Для прихожей")
    office = models.BooleanField(verbose_name="Для офиса")
    state = models.ForeignKey(AudioState, on_delete=models.PROTECT, verbose_name="Состояние")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Вешалку/прихожую"
        verbose_name_plural = "Вешалки, прихожие"

# _______ Комоды ________
class Dresser(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Мебель")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Комоды")
    living_room = models.BooleanField(verbose_name="Для гостиной")
    bedroom = models.BooleanField(verbose_name="Для спальни")
    kitchen = models.BooleanField(verbose_name="Для кухни")
    bathroom = models.BooleanField(verbose_name="Для ванной комнаты")
    hallway = models.BooleanField(verbose_name="Для прихожей")
    office = models.BooleanField(verbose_name="Для офиса")
    state = models.ForeignKey(AudioState, on_delete=models.PROTECT, verbose_name="Состояние")
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена")
    exchange = models.BooleanField(verbose_name="Возможен обмен")
    installment_plan = models.BooleanField(verbose_name="Готов(а) продать товар в рассрочку")
    city = models.CharField(max_length=200, verbose_name="Город", choices=CITY)
    grade = models.FloatField(verbose_name="Оценка", default=0)
    user_create = models.ForeignKey(User, verbose_name="Пользователь, создавший запись", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Комод"
        verbose_name_plural = "Комоды"
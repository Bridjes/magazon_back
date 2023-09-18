from django.db import models
from users.models import User
from .models_lists import *

########## АВТО И ТРАНСПОРТ ###########

# ___________легковые авто_____________
class Car(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='Car', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Авто и транспорт")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Легковые авто")
    brand = models.CharField(max_length=100, verbose_name="Марка", choices=CAR_BRAND)
    model = models.CharField(max_length=100, verbose_name="Модель", choices=CAR_MODEl)
    body_type = models.CharField(max_length=200, verbose_name="Тип кузова", choices=CAR_BODY_TYPE)
    color = models.CharField(max_length=200, verbose_name="Цвет", choices=CAR_COLOR)
    engine_type = models.CharField(max_length=200, verbose_name="Тип двигателя", choices=CAR_ENGIN_TYPE)
    drive_unit = models.CharField(max_length=200, verbose_name="Привод", choices=CAR_DRIVE_UNIT)
    transmission = models.CharField(max_length=200, verbose_name="Коробка передач", choices=CAR_TRANSMISSION)
    engine_volume = models.CharField(max_length=200, verbose_name="Объём двигателя", choices=CAR_ENGINE_VOLUME)
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
class Truck(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='Truck', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Авто и транспорт")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Грузовики и автобусы")
    brand = models.CharField(max_length=100, verbose_name="Марка", choices=TRUCK_BRAND)
    type = models.CharField(max_length=200, verbose_name="Тип грузовика", choices=TRUCK_TYPE)
    load_capacity = models.CharField(max_length=200, verbose_name="Грузоподъемность", choices=TRUCK_LOAD_CAPACITY)
    transmission = models.CharField(max_length=200, verbose_name="Коробка передач", choices=TRUCK_TRANSMISSION)
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
# мотоциклы
class Motorbike(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='Motobike', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Авто и транспорт")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Мотоциклы")
    brand = models.CharField(max_length=100, verbose_name="Марка", choices=MOTOBIKE_BRAND)
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
class Apartment(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='Apartment', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Недвижимость")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Квартиры")
    deal_type = models.CharField(max_length=50, verbose_name="Тип сделки", choices=APARTMENT_DEAL_TYPE)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    rooms = models.CharField(max_length=50, verbose_name="Количество комнат", choices=APARTMENT_ROOMS)
    layout = models.CharField(max_length=50, verbose_name="Вид планировки", choices=APARTMENT_LAYOUT)
    floors = models.CharField(max_length=50, verbose_name="Этажность дома", choices=APARTMENT_FLOORS)
    ceiling_height = models.CharField(max_length=50, verbose_name="Высота потолков", choices=APARTMENT_CEILING_HEIGHT)
    wall_material = models.CharField(max_length=50, verbose_name="Материал стен", choices=APARTMENT_WALL_MATERIAL)
    salesman = models.CharField(max_length=50, verbose_name="Продавец", choices=APARTMENT_SALESMAN)
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
    photo = models.ImageField(upload_to='Cottage', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Недвижимость")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Дома, дачи, коттеджи")
    deal_type = models.CharField(max_length=50, verbose_name="Тип сделки", choices=APARTMENT_DEAL_TYPE)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    salesman = models.CharField(max_length=50, verbose_name="Продавец", choices=APARTMENT_SALESMAN)
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
    photo = models.ImageField(upload_to='Garage', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Недвижимость")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Гаражи и стоянки")
    deal_type = models.CharField(max_length=50, verbose_name="Тип сделки", choices=APARTMENT_DEAL_TYPE)
    address = models.CharField(max_length=255, verbose_name="Адрес")
    salesman = models.CharField(max_length=50, verbose_name="Продавец", choices=APARTMENT_SALESMAN)
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
class Audio(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='Audio', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Электроника")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Аудиотехника")
    type = models.CharField(max_length=200, verbose_name="Тип", choices=AUDIO_TYPE)
    state = models.CharField(max_length=50, verbose_name="Состояние", choices=AUDIO_STATE)
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
class Headphones(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='Headphones', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Электроника")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Наушники")
    type = models.CharField(max_length=100, verbose_name="Тип", choices=HEADPHONES_TYPE)
    wireless = models.BooleanField(verbose_name="Беспроводные")
    brand = models.CharField(max_length=100, verbose_name="Производитель", choices=HEADPHONES_BRAND)
    connector = models.CharField(max_length=100, verbose_name="Тип разъёма", choices=HEADPHONES_CONNECTOR)
    purpose = models.CharField(max_length=100, verbose_name="Назначение", choices=HEADPHONES_PURPOSE)
    fastening = models.CharField(max_length=100, verbose_name="Крепление", choices=HEADPHONES_FASTENING)
    noise_reduction = models.BooleanField(verbose_name="Активное шумоподавление")
    surround_sound = models.BooleanField(verbose_name="Объёмное звучание")
    folding = models.BooleanField(verbose_name="Возможность складывания")
    volume_control = models.BooleanField(verbose_name="Регулировка громкости")
    protection = models.BooleanField(verbose_name="Пыле- и влагозащита")
    microphone = models.BooleanField(verbose_name="Микрофон")
    NFC = models.BooleanField(verbose_name="NFC")
    state = models.CharField(max_length=50, verbose_name="Состояние", choices=AUDIO_STATE)
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
class VideoEquipment(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='VideoEquipment', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Электроника")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="ТВ и видеотехника")
    type = models.CharField(max_length=100, verbose_name="Тип", choices=VIDEO_EQUIPMENT_TYPE)
    manufacturer = models.CharField(max_length=100, verbose_name="Производитель", choices=VIDEO_EQUIPMENT_BRAND)
    state = models.CharField(max_length=50, verbose_name="Состояние", choices=AUDIO_STATE)
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
class Ottomans(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='Ottomans', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Мебель")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Банкетки и пуфики")
    type = models.CharField(max_length=50, verbose_name="Тип", choices=OTTOMANS_TYPE)
    box = models.BooleanField(verbose_name="С ящиком")
    living_room = models.BooleanField(verbose_name="Для гостиной")
    bedroom = models.BooleanField(verbose_name="Для спальни")
    kitchen = models.BooleanField(verbose_name="Для кухни")
    bathroom = models.BooleanField(verbose_name="Для ванной комнаты")
    hallway = models.BooleanField(verbose_name="Для прихожей")
    office = models.BooleanField(verbose_name="Для офиса")
    state = models.CharField(max_length=50, verbose_name="Состояние", choices=AUDIO_STATE)
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
class Hanger(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Название товара/услуги")
    photo = models.ImageField(upload_to='Hanger', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Мебель")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Вешалки, прихожие")
    type = models.CharField(max_length=50, verbose_name="Тип", choices=HEADPHONES_TYPE)
    fastening = models.CharField(max_length=50, verbose_name="Способ крепления", choices=HEADPHONES_FASTENING)
    living_room = models.BooleanField(verbose_name="Для гостиной")
    bedroom = models.BooleanField(verbose_name="Для спальни")
    kitchen = models.BooleanField(verbose_name="Для кухни")
    bathroom = models.BooleanField(verbose_name="Для ванной комнаты")
    hallway = models.BooleanField(verbose_name="Для прихожей")
    office = models.BooleanField(verbose_name="Для офиса")
    state = models.CharField(max_length=50, verbose_name="Состояние", choices=AUDIO_STATE)
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
    photo = models.ImageField(upload_to='Dresser', null=True)
    category = models.CharField(max_length=100, verbose_name="Категория", choices=CATEGORY, default="Мебель")
    subcategory = models.CharField(max_length=100, verbose_name="Подкатегория", choices=SUBCATEGORY, default="Комоды")
    living_room = models.BooleanField(verbose_name="Для гостиной")
    bedroom = models.BooleanField(verbose_name="Для спальни")
    kitchen = models.BooleanField(verbose_name="Для кухни")
    bathroom = models.BooleanField(verbose_name="Для ванной комнаты")
    hallway = models.BooleanField(verbose_name="Для прихожей")
    office = models.BooleanField(verbose_name="Для офиса")
    state = models.CharField(max_length=50, verbose_name="Состояние", choices=AUDIO_STATE)
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
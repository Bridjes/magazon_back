from django.contrib import admin
from .models import *

######## Транспорт ########
#_____ Легковые авто ______

class CarModelInline(admin.TabularInline):
    model = CarModel

# марка легкового авто
@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name',)
    search_fields = ('name',)

# модель легкового авто
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_brand')
    search_fields = ('name', 'car_brand__name')

# легковые авто
@admin.register(Car)
class CarsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Car._meta.get_fields()]

#_____ Грузовые авто ______

# марка грузового авто
@admin.register(TruckBrand)
class TruckBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# грузовые авто
@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Truck._meta.get_fields()]

#_______ Мотоциклы _________

# марки мотоциклов
@admin.register(MotorbikeBrand)
class TruckBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# мотоциклы
@admin.register(Motorbike)
class MotorbikeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Motorbike._meta.get_fields()]


######## НЕДВИЖИМОСТЬ ########

# ________ Квартиры __________
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Apartment._meta.get_fields()]

# ___ Дома, дачи, коттеджи ____
@admin.register(Cottage)
class CottageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cottage._meta.get_fields()]

# _____ Гаражи и стоянки ______
@admin.register(Garage)
class GarageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Garage._meta.get_fields()]


######## ЭЛЕКТРОНИКА ########

# ______ Аудиотехника _______
@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Audio._meta.get_fields()]

# ________ Наушники __________

# производитель наушников
@admin.register(HeadphonesBrand)
class HeadphonesBrandAdmin(admin.ModelAdmin):
    list_display = ('value',)
    search_fields = ('value',)

# наушники
@admin.register(Headphones)
class HeadphonesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Headphones._meta.get_fields()]

# ________ ТВ и видеотехника __________

class VideoEquipmentManufacturerInline(admin.TabularInline):
    model = VideoEquipmentManufacturer

# тип
@admin.register(VideoEquipmentType)
class VideoEquipmentTypeAdmin(admin.ModelAdmin):
    inlines = [VideoEquipmentManufacturerInline]
    list_display = ('value',)

# производитель
@admin.register(VideoEquipmentManufacturer)
class VideoEquipmentManufacturerAdmin(admin.ModelAdmin):
    list_display = ('value', 'type')
    search_fields = ('value', 'type')

# ТВ и видеотехника
@admin.register(VideoEquipment)
class VideoEquipmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in VideoEquipment._meta.get_fields()]

############## МЕБЕЛЬ ##############

# _______ банкетки и пуфики ________
@admin.register(Ottomans)
class OttomansAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ottomans._meta.get_fields()]

# _______ Вешалки, прихожие ________
@admin.register(Hanger)
class HangerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hanger._meta.get_fields()]

# _______ Комоды ________
@admin.register(Dresser)
class DresserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dresser._meta.get_fields()]
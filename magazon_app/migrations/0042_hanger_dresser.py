# Generated by Django 4.2.4 on 2023-09-07 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazon_app', '0041_delete_hanger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hanger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название товара/услуги')),
                ('living_room', models.BooleanField(verbose_name='Для гостиной')),
                ('bedroom', models.BooleanField(verbose_name='Для спальни')),
                ('kitchen', models.BooleanField(verbose_name='Для кухни')),
                ('bathroom', models.BooleanField(verbose_name='Для ванной комнаты')),
                ('hallway', models.BooleanField(verbose_name='Для прихожей')),
                ('office', models.BooleanField(verbose_name='Для офиса')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('exchange', models.BooleanField(verbose_name='Возможен обмен')),
                ('installment_plan', models.BooleanField(verbose_name='Готов(а) продать товар в рассрочку')),
                ('grade', models.FloatField(default=0, verbose_name='Оценка')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.subcategory', verbose_name='Категория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.city', verbose_name='Город')),
                ('fastening', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.hangerfastening', verbose_name='Способ крепления')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.audiostate', verbose_name='Состояние')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.hangertype', verbose_name='Тип')),
                ('user_create', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, создавший запись')),
            ],
            options={
                'verbose_name': 'Вешалку/прихожую',
                'verbose_name_plural': 'Вешалки, прихожие',
            },
        ),
        migrations.CreateModel(
            name='Dresser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название товара/услуги')),
                ('living_room', models.BooleanField(verbose_name='Для гостиной')),
                ('bedroom', models.BooleanField(verbose_name='Для спальни')),
                ('kitchen', models.BooleanField(verbose_name='Для кухни')),
                ('bathroom', models.BooleanField(verbose_name='Для ванной комнаты')),
                ('hallway', models.BooleanField(verbose_name='Для прихожей')),
                ('office', models.BooleanField(verbose_name='Для офиса')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('exchange', models.BooleanField(verbose_name='Возможен обмен')),
                ('installment_plan', models.BooleanField(verbose_name='Готов(а) продать товар в рассрочку')),
                ('grade', models.FloatField(default=0, verbose_name='Оценка')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.subcategory', verbose_name='Категория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.city', verbose_name='Город')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.audiostate', verbose_name='Состояние')),
                ('user_create', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, создавший запись')),
            ],
            options={
                'verbose_name': 'Комод',
                'verbose_name_plural': 'Комоды',
            },
        ),
    ]

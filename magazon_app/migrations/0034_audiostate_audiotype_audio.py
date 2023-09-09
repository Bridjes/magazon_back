# Generated by Django 4.2.4 on 2023-09-06 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazon_app', '0033_garage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150, unique=True, verbose_name='Состояние')),
            ],
            options={
                'verbose_name': 'Состояние',
                'verbose_name_plural': 'Аудиотехника - Состояние',
            },
        ),
        migrations.CreateModel(
            name='AudioType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150, unique=True, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Аудиотехника - Типы',
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название товара/услуги')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('exchange', models.BooleanField(verbose_name='Возможен обмен')),
                ('installment_plan', models.BooleanField(verbose_name='Готов(а) продать товар в рассрочку')),
                ('grade', models.FloatField(default=0, verbose_name='Оценка')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.subcategory', verbose_name='Категория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.city', verbose_name='Город')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.audiostate', verbose_name='Состояние')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magazon_app.audiotype', verbose_name='Тип')),
                ('user_create', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, создавший запись')),
            ],
            options={
                'verbose_name': 'Мотоцикл',
                'verbose_name_plural': 'Мотоциклы',
            },
        ),
    ]
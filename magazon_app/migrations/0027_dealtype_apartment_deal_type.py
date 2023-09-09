# Generated by Django 4.2.4 on 2023-09-06 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazon_app', '0026_alter_apartment_category_alter_car_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(unique=True, verbose_name='Тип сделки')),
            ],
            options={
                'verbose_name': 'Тип сделки',
                'verbose_name_plural': 'Квартиры - Тип сделки',
            },
        ),
        migrations.AddField(
            model_name='apartment',
            name='deal_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.dealtype', verbose_name='Тип сделки'),
        ),
    ]
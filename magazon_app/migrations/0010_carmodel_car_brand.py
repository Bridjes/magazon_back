# Generated by Django 4.2.4 on 2023-09-04 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazon_app', '0009_alter_city_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='car_brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.carbrand', verbose_name='Марка'),
        ),
    ]

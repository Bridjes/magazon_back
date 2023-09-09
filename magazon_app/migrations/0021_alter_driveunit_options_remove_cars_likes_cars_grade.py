# Generated by Django 4.2.4 on 2023-09-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazon_app', '0020_cars_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driveunit',
            options={'verbose_name': 'Привод', 'verbose_name_plural': 'Типы привода'},
        ),
        migrations.RemoveField(
            model_name='cars',
            name='likes',
        ),
        migrations.AddField(
            model_name='cars',
            name='grade',
            field=models.FloatField(default=0, verbose_name='Оценка'),
        ),
    ]

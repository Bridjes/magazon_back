# Generated by Django 4.2.4 on 2023-09-06 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazon_app', '0029_alter_apartmentceilingheight_value_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'Квартиру', 'verbose_name_plural': 'Квартиры'},
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-04 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazon_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегорию', 'verbose_name_plural': 'Подкатегории'},
        ),
    ]

# Generated by Django 4.2.4 on 2023-09-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazon_app', '0046_remove_cartest_brand_remove_cartest_model_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Audi', 'Audi'), ('Volkswagen', 'Volkswagen'), ('00', '00')], max_length=100, verbose_name='Название поля')),
            ],
        ),
    ]
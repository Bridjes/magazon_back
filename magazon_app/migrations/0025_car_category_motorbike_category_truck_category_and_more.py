# Generated by Django 4.2.4 on 2023-09-06 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazon_app', '0024_apartmentceilingheight_apartmentfloors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='motorbike',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='truck',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='magazon_app.category', verbose_name='Категория'),
        ),
    ]
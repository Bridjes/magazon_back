# Generated by Django 4.2.4 on 2023-09-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazon_app', '0052_alter_truck_truck_load_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motorbike',
            name='number_cycles',
            field=models.CharField(choices=[('2', '2'), ('4', '4')], max_length=50, verbose_name='Количество тактов'),
        ),
        migrations.AlterField(
            model_name='motorbike',
            name='number_cylinders',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('6', '6')], max_length=50, verbose_name='Количество цилиндров'),
        ),
        migrations.AlterField(
            model_name='motorbike',
            name='number_volume',
            field=models.CharField(choices=[('16', '16'), ('40', '40'), ('48', '48'), ('49', '49'), ('50', '50'), ('60', '60'), ('64', '64'), ('70', '70'), ('72', '72'), ('84', '84'), ('97', '97'), ('99', '99'), ('100', '100'), ('107', '107'), ('110', '110'), ('112', '112'), ('123', '123'), ('124', '124'), ('125', '125'), ('140', '140'), ('145', '145'), ('149', '149'), ('150', '150'), ('158', '158'), ('160', '160'), ('190', '190'), ('196', '196'), ('197', '197'), ('198', '198'), ('200', '200'), ('210', '210'), ('220', '220'), ('223', '223'), ('224', '224'), ('225', '225'), ('233', '233'), ('249', '249'), ('250', '250'), ('270', '270'), ('271', '271'), ('275', '275'), ('279', '279'), ('298', '298'), ('300', '300'), ('313', '313'), ('321', '321'), ('350', '350'), ('352', '352'), ('373', '373'), ('399', '399'), ('400', '400'), ('449', '449'), ('450', '450'), ('471', '471'), ('493', '493'), ('495', '495'), ('499', '499'), ('500', '500'), ('550', '550'), ('570', '570'), ('580', '580'), ('600', '600'), ('636', '636'), ('649', '649'), ('650', '650'), ('689', '689'), ('695', '695'), ('700', '700'), ('749', '749'), ('750', '750'), ('800', '800'), ('847', '847'), ('900', '900'), ('942', '942'), ('948', '948'), ('976', '976'), ('998', '998'), ('1000', '1000'), ('1043', '1043'), ('1200', '1200'), ('1298', '1298'), ('1500', '1500'), ('1679', '1679'), ('2000', '2000'), ('2500', '2500')], max_length=50, verbose_name='Объём, см³'),
        ),
        migrations.AlterField(
            model_name='motorbike',
            name='truck_dive_unit',
            field=models.CharField(choices=[('Кардан', 'Кардан'), ('Ремень', 'Ремень'), ('Цепь', 'Цепь')], max_length=50, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='motorbike',
            name='type',
            field=models.CharField(choices=[('Кастом', 'Кастом'), ('Классик', 'Классик'), ('Кроссовый', 'Кроссовый'), ('Круизер/Чоппер', 'Круизер/Чоппер'), ('Мотард', 'Мотард'), ('Пит-байк', 'Пит-байк'), ('Спорт', 'Спорт'), ('Спорт-турист', 'Спорт-турист'), ('Стрит', 'Стрит'), ('Трайк', 'Трайк'), ('Туризм', 'Туризм'), ('Эндуро', 'Эндуро')], max_length=50, verbose_name='Тип мотоцикла'),
        ),
        migrations.DeleteModel(
            name='MotorbikeDriveUnit',
        ),
        migrations.DeleteModel(
            name='MotorbikeNumberCycles',
        ),
        migrations.DeleteModel(
            name='MotorbikeNumberCylinders',
        ),
        migrations.DeleteModel(
            name='MotorbikeType',
        ),
        migrations.DeleteModel(
            name='MotorbikeVolume',
        ),
    ]

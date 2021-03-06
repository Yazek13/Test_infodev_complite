# Generated by Django 3.2.5 on 2021-07-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_alter_device_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='category',
        ),
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.CharField(choices=[('Сирена', 'Сирена'), ('Громкоговоритель', 'Громкоговоритель')], default=('Сирена', 'Сирена'), max_length=16, verbose_name='Тип устройства'),
        ),
        migrations.AlterField(
            model_name='device',
            name='radius',
            field=models.IntegerField(verbose_name='Радиус зоны звукопокрытия'),
        ),
    ]

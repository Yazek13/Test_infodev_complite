# Generated by Django 3.2.5 on 2021-07-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20210727_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(choices=[('SR', 'Сирена'), ('SP', 'Громкоговоритель')], default=('SR', 'Сирена'), max_length=16, verbose_name='Тип устройства'),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-24 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_venta_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='estado_envio',
            field=models.CharField(default='EN PREPARACION', max_length=15),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 23, 22, 12, 56, 395533)),
        ),
    ]

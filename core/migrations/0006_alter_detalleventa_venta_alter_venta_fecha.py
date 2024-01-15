# Generated by Django 4.2.2 on 2023-06-16 19:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_detalleventa_venta_alter_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.venta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 16, 15, 14, 26, 540878)),
        ),
    ]

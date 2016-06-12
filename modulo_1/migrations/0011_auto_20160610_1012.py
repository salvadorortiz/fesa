# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0010_auto_20160604_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='remesaxreserva',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2016, 6, 10, 10, 12, 2, 680980), verbose_name=b'Fecha de ingreso', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_ingreso',
            field=models.DateField(default=datetime.datetime(2016, 6, 10, 10, 12, 10, 608900), verbose_name=b'Fecha de ingreso', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservacancha',
            name='precio_sugerido',
            field=models.DecimalField(default=0.0, verbose_name=b'Precio Sugerido', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(default=b'', max_length=1, verbose_name=b'Dias', choices=[(b'C', b'Confirmado'), (b'T', b'Tentativo'), (b'R', b'Realizado'), (b'N', b'No realizado')]),
        ),
    ]

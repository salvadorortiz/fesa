# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0019_auto_20160705_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='forma_facturacion',
            field=models.ForeignKey(verbose_name=b'Forma de facturaci\xc3\xb3n', blank=True, to='modulo_1.FormaFacturacion', null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='area',
            field=models.CharField(max_length=100, verbose_name=b'\xc3\x81rea'),
        ),
    ]

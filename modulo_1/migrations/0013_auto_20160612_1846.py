# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0012_auto_20160610_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ingresado_por',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name=b'IngresadoPor', blank=True),
        ),
        migrations.AddField(
            model_name='empresa',
            name='ingresado_por',
            field=models.CharField(default=b'', max_length=20, null=True, verbose_name=b'IngresadoPor', blank=True),
        ),
    ]

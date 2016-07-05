# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0016_reservacancha_precio_acordado'),
    ]

    operations = [
        migrations.AddField(
            model_name='remesaxreserva',
            name='banco',
            field=models.CharField(default=b'', max_length=150, null=True, verbose_name=b'Banco', blank=True),
        ),
    ]

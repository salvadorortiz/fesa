# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0018_reserva_bandera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='bandera',
            field=models.BooleanField(default=False, verbose_name=b'Bandera'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0017_remesaxreserva_banco'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='bandera',
            field=models.BooleanField(default=True, verbose_name=b'Bandera'),
        ),
    ]

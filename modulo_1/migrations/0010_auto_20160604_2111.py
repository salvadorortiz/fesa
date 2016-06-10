# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0009_auto_20160603_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='remesaxreserva',
            name='usuario',
            field=models.ForeignKey(default=1, verbose_name=b'Usuario', to='modulo_1.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='usuario',
            field=models.ForeignKey(default=1, verbose_name=b'Usuario', to='modulo_1.Usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservacancha',
            name='usuario',
            field=models.ForeignKey(default=1, verbose_name=b'Usuario', to='modulo_1.Usuario'),
            preserve_default=False,
        ),
    ]

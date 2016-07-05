# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0015_remove_usuario_password_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacancha',
            name='precio_acordado',
            field=models.DecimalField(default=0.0, verbose_name=b'Precio Acordado', max_digits=10, decimal_places=2),
        ),
    ]

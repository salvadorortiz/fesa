# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0013_auto_20160612_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='password_default',
            field=models.BooleanField(default=True, verbose_name=b'Contrase\xc3\xb1a por Defecto'),
        ),
    ]

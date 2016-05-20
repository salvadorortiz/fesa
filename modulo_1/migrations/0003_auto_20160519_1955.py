# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0002_auto_20160515_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='area',
            field=models.CharField(max_length=50, verbose_name=b'\xc3\x81rea'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=b'123', max_length=100, verbose_name=b'Contrase\xc3\xb1a'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'Usuario'),
        ),
    ]

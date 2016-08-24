# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0020_auto_20160708_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacancha',
            name='media_cancha',
            field=models.BooleanField(default=False, verbose_name=b'Media cancha'),
        ),
    ]

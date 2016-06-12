# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0011_auto_20160610_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservacancha',
            old_name='hora',
            new_name='hora_fin',
        ),
        migrations.AddField(
            model_name='reservacancha',
            name='hora_inicio',
            field=models.TimeField(default=datetime.datetime(2016, 6, 10, 23, 5, 14, 663578)),
            preserve_default=False,
        ),
    ]

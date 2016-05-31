# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0007_auto_20160527_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='precioxcancha',
            name='hora',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'Hora'),
        ),
    ]

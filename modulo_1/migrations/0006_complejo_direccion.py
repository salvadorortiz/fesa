# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0005_auto_20160520_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='complejo',
            name='direccion',
            field=models.TextField(max_length=250, null=True, verbose_name=b'Direcci\xc3\xb3n', blank=True),
        ),
    ]

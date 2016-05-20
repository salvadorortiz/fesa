# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0003_auto_20160519_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.TextField(max_length=250, null=True, verbose_name=b'Direcci\xc3\xb3n', blank=True),
        ),
    ]

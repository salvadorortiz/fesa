# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(blank=True, max_length=60, null=True, verbose_name=b'Correo electr\xc3\xb3nico', validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=15, verbose_name=b'Tel\xc3\xa9fono', validators=[django.core.validators.RegexValidator(regex=b'^(([(][0-9]+[)])( |[0-9-]+)+([ ](ext|EXT)[ ][0-9]+)(,|-)?)+$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido: (503) 2256 45 54 EXT 123 \xc3\xb3 (503) 2256-4554 EXT 123')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_alterno',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name=b'Tel\xc3\xa9fono alterno', validators=[django.core.validators.RegexValidator(regex=b'^(([(][0-9]+[)])( |[0-9-]+)+([ ](ext|EXT)[ ][0-9]+)(,|-)?)+$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido: (503) 2256 45 54 EXT 123 \xc3\xb3 (503) 2256-4554 EXT 123')]),
        ),
    ]

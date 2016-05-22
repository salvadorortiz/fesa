# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0004_auto_20160519_2107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='user',
            new_name='usuario',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=15, verbose_name=b'Tel\xc3\xa9fono', validators=[django.core.validators.RegexValidator(regex=b'^([(][0-9]+[)]) ([0-9-][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9])$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido')]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_alterno',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name=b'Tel\xc3\xa9fono alterno', validators=[django.core.validators.RegexValidator(regex=b'^([(][0-9]+[)]) ([0-9-][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9])$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido')]),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name=b'Tel\xc3\xa9fono', validators=[django.core.validators.RegexValidator(regex=b'^([(][0-9]+[)]) ([0-9-][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9])$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido')]),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='telefono_contacto',
            field=models.CharField(max_length=50, verbose_name=b'Tel\xc3\xa9fono de contacto', validators=[django.core.validators.RegexValidator(regex=b'^([(][0-9]+[)]) ([0-9-][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9])$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Contrase\xc3\xb1a'),
        ),
    ]

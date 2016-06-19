# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0014_usuario_password_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='password_default',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0006_complejo_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrecioXCancha',
            fields=[
                ('precio_cancha_id', models.AutoField(serialize=False, primary_key=True)),
                ('precio', models.DecimalField(default=0.0, verbose_name=b'Precio', max_digits=10, decimal_places=2)),
                ('dias', models.CharField(default=b'', max_length=200, verbose_name=b'D\xc3\xadas')),
            ],
        ),
        migrations.RemoveField(
            model_name='cancha',
            name='precio',
        ),
        migrations.AddField(
            model_name='precioxcancha',
            name='cancha',
            field=models.ForeignKey(verbose_name=b'Cancha', to='modulo_1.Cancha'),
        ),
    ]

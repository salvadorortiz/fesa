# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('modulo_1', '0008_precioxcancha_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemesaXReserva',
            fields=[
                ('remesa_reserva_id', models.AutoField(serialize=False, primary_key=True)),
                ('numero_remesa', models.CharField(default=b'', max_length=100, verbose_name=b'N\xc3\xbamero de remesa')),
                ('monto', models.DecimalField(default=0.0, verbose_name=b'Monto', max_digits=10, decimal_places=2)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='horariocomplejo',
            name='complejo',
        ),
        migrations.RemoveField(
            model_name='precioxcancha',
            name='dias',
        ),
        migrations.RemoveField(
            model_name='precioxcancha',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='remanente',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='remesado',
        ),
        migrations.AddField(
            model_name='precioxcancha',
            name='dia',
            field=models.CharField(default=b'', max_length=1, verbose_name=b'Dia', choices=[(b'X', b'Lunes-Viernes'), (b'S', b'S\xc3\xa1bado'), (b'D', b'Domingo')]),
        ),
        migrations.AddField(
            model_name='precioxcancha',
            name='hora_apertura',
            field=models.TimeField(default=datetime.datetime(2016, 6, 3, 22, 54, 50, 379782)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='precioxcancha',
            name='hora_cierre',
            field=models.TimeField(default=datetime.datetime(2016, 6, 3, 22, 55, 8, 171357)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='saldo',
            field=models.DecimalField(default=0.0, verbose_name=b'Saldo', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cancha',
            name='horas_posibles',
            field=models.IntegerField(default=0, verbose_name=b'Horas posibles'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='costo',
            field=models.DecimalField(null=True, verbose_name=b'Costo', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='precio',
            field=models.DecimalField(null=True, verbose_name=b'Precio', max_digits=10, decimal_places=2, blank=True),
        ),
        migrations.DeleteModel(
            name='HorarioComplejo',
        ),
        migrations.AddField(
            model_name='remesaxreserva',
            name='reserva',
            field=models.ForeignKey(verbose_name=b'Reserva', to='modulo_1.Reserva'),
        ),
    ]

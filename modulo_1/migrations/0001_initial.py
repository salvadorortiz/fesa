# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('cancha_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
                ('precio', models.DecimalField(default=0.0, verbose_name=b'Precio', max_digits=10, decimal_places=2)),
                ('horas_posibles', models.IntegerField(default=0, verbose_name=b'Horas posibles', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('cliente_id', models.AutoField(serialize=False, primary_key=True)),
                ('codigo', models.CharField(default=b'', max_length=20, null=True, verbose_name=b'C\xc3\xb3digo', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
                ('DUI', models.CharField(default=b'', max_length=10, null=True, verbose_name=b'DUI', blank=True)),
                ('telefono', models.CharField(max_length=50, verbose_name=b'Tel\xc3\xa9fono', validators=[django.core.validators.RegexValidator(regex=b'^(([(][0-9]+[)])( |[0-9-]+)+([ ](ext|EXT)[ ][0-9]+)(,|-)?)+$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido: (503) 2256 45 54 EXT 123 \xc3\xb3 (503) 2256-4554 EXT 123')])),
                ('telefono_alterno', models.CharField(blank=True, max_length=50, verbose_name=b'Tel\xc3\xa9fono alterno', validators=[django.core.validators.RegexValidator(regex=b'^(([(][0-9]+[)])( |[0-9-]+)+([ ](ext|EXT)[ ][0-9]+)(,|-)?)+$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido: (503) 2256 45 54 EXT 123 \xc3\xb3 (503) 2256-4554 EXT 123')])),
                ('correo', models.EmailField(blank=True, max_length=60, verbose_name=b'Correo electr\xc3\xb3nico', validators=[django.core.validators.EmailValidator()])),
                ('direccion', models.TextField(max_length=250, verbose_name=b'Direcci\xc3\xb3n', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Complejo',
            fields=[
                ('complejo_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresa_id', models.AutoField(serialize=False, primary_key=True)),
                ('codigo', models.CharField(default=b'', max_length=20, null=True, verbose_name=b'C\xc3\xb3digo', blank=True)),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
                ('nit', models.CharField(default=b'', max_length=17, verbose_name=b'Nombre')),
                ('registro_iva', models.CharField(default=b'', max_length=50, verbose_name=b'Registro')),
                ('telefono', models.CharField(max_length=50, verbose_name=b'Tel\xc3\xa9fono', validators=[django.core.validators.RegexValidator(regex=b'^(([(][0-9]+[)])( |[0-9-]+)+([ ](ext|EXT)[ ][0-9]+)(,|-)?)+$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido: (503) 2256 45 54 EXT 123 \xc3\xb3 (503) 2256-4554 EXT 123')])),
                ('contacto', models.CharField(default=b'', max_length=100, verbose_name=b'Persona de contacto')),
                ('telefono_contacto', models.CharField(max_length=50, verbose_name=b'Tel\xc3\xa9fono de contacto', validators=[django.core.validators.RegexValidator(regex=b'^(([(][0-9]+[)])( |[0-9-]+)+([ ](ext|EXT)[ ][0-9]+)(,|-)?)+$', message=b'El tel\xc3\xa9fono no cumple con un formato v\xc3\xa1lido: (503) 2256 45 54 EXT 123 \xc3\xb3 (503) 2256-4554 EXT 123')])),
                ('correo_contacto', models.EmailField(blank=True, max_length=60, verbose_name=b'Correo electr\xc3\xb3nico de contacto', validators=[django.core.validators.EmailValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='FormaFacturacion',
            fields=[
                ('forma_facturacion_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('forma_pago_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioComplejo',
            fields=[
                ('horario_complejo_id', models.AutoField(serialize=False, primary_key=True)),
                ('dia', models.CharField(default=b'', max_length=1, verbose_name=b'Dias', choices=[(b'L', b'Lunes'), (b'M', b'Martes'), (b'X', b'Mi\xc3\xa9rcoles'), (b'J', b'Jueves'), (b'V', b'Viernes'), (b'S', b'S\xc3\xa1bado'), (b'D', b'Domingo')])),
                ('hora_apertura', models.TimeField()),
                ('hora_cierre', models.TimeField()),
                ('complejo', models.ForeignKey(related_name='complejo', verbose_name=b'Complejo', to='modulo_1.Complejo')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('reserva_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_evento', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre del evento')),
                ('estado', models.CharField(default=b'', max_length=1, verbose_name=b'Dias', choices=[(b'C', b'Confirmado'), (b'T', b'Tentativo')])),
                ('precio', models.DecimalField(default=0.0, verbose_name=b'Precio', max_digits=10, decimal_places=2)),
                ('costo', models.DecimalField(default=0.0, verbose_name=b'Costo', max_digits=10, decimal_places=2)),
                ('remesado', models.DecimalField(default=0.0, verbose_name=b'Remesado', max_digits=10, decimal_places=2)),
                ('remanente', models.DecimalField(default=0.0, verbose_name=b'Remanente', max_digits=10, decimal_places=2)),
                ('notas', models.TextField(max_length=500, null=True, verbose_name=b'\xc3\x81rea', blank=True)),
                ('cliente', models.ForeignKey(verbose_name=b'Cliente', blank=True, to='modulo_1.Cliente', null=True)),
                ('empresa', models.ForeignKey(verbose_name=b'Empresa', blank=True, to='modulo_1.Empresa', null=True)),
                ('forma_facturacion', models.ForeignKey(verbose_name=b'Forma de facturaci\xc3\xb3n', to='modulo_1.FormaFacturacion')),
                ('forma_pago', models.ForeignKey(verbose_name=b'Forma de pago', to='modulo_1.FormaPago')),
            ],
        ),
        migrations.CreateModel(
            name='ReservaCancha',
            fields=[
                ('reserva_cancha_id', models.AutoField(serialize=False, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('notas', models.TextField(max_length=500, null=True, verbose_name=b'\xc3\x81rea', blank=True)),
                ('cancha', models.ForeignKey(verbose_name=b'Cancha', to='modulo_1.Cancha')),
                ('reserva', models.ForeignKey(verbose_name=b'Reserva', to='modulo_1.Reserva')),
            ],
        ),
        migrations.CreateModel(
            name='TipoAlquiler',
            fields=[
                ('tipo_alquiler_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario_id', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
                ('area', models.TextField(max_length=50, verbose_name=b'\xc3\x81rea')),
                ('jefe_directo', models.CharField(default=b'', max_length=100, verbose_name=b'Jefe Directo')),
                ('estado', models.BooleanField(default=True, verbose_name=b'Estado')),
                ('tipo_usuario', models.CharField(default=b'', max_length=1, verbose_name=b'Tipo Usuario', choices=[(b'A', b'Tipo A'), (b'B', b'Tipo B'), (b'R', b'Administrador')])),
                ('user', models.CharField(default=b'', max_length=50, verbose_name=b'Nombre')),
                ('password', models.CharField(default=b'123', max_length=50, verbose_name=b'Contrase\xc3\xb1a')),
            ],
        ),
        migrations.AddField(
            model_name='reserva',
            name='tipo_alquiler',
            field=models.ForeignKey(verbose_name=b'Tipo de alquiler', to='modulo_1.TipoAlquiler'),
        ),
        migrations.AddField(
            model_name='cancha',
            name='complejo',
            field=models.ForeignKey(verbose_name=b'Complejo', to='modulo_1.Complejo'),
        ),
    ]

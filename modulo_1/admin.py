# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *

#class MedicoAdmin(admin.ModelAdmin):
#	list_display =('nombre','especialidad')
#class ConsultaAdmin(admin.ModelAdmin):
#	list_display =('fecha','paciente','medico')
#class UsuarioAdmin(admin.ModelAdmin):
#	list_display =('user','password','medico','paciente','estado')

#admin.site.register(Medico, MedicoAdmin)
#admin.site.register(Paciente)
#admin.site.register(Consulta,ConsultaAdmin)
#admin.site.register(Usuario,UsuarioAdmin)

admin.site.register(Usuario)
admin.site.register(Complejo)
admin.site.register(HorarioComplejo)
admin.site.register(Cancha)
admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(FormaPago)
admin.site.register(FormaFacturacion)
admin.site.register(TipoAlquiler)
admin.site.register(Reserva)
admin.site.register(ReservaCancha)

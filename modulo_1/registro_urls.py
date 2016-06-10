from django.conf.urls import include, url
from django.contrib import admin
from modulo_1 import cliente_views, datosbase_views

urlpatterns = [
    url(r'^cliente/', 'modulo_1.cliente_views.RegistroClienteView',name='cliente_registrocliente'),
    url(r'^precios/', 'modulo_1.views.PreciosView',name='precios_guia'),
    url(r'^precios_vista/', 'modulo_1.views.dt_precios',name='dt_precios'),
    url(r'^actualizar_precio/', 'modulo_1.views.GuardarPrecio',name='guardar_precio'),
    url(r'^autenticacion/', 'modulo_1.views.Autenticacion',name='autenticacion'),
    url(r'^guardar_cliente/', 'modulo_1.cliente_views.GuardarCliente',name='guardar_cliente'),
    url(r'^clientes_vista/', 'modulo_1.cliente_views.dt_clientes',name='dt_clientes'),
    url(r'^cargar_cliente/', 'modulo_1.cliente_views.CargarCliente',name='cargar_cliente'),
    url(r'^guardar_cambios_cliente/', 'modulo_1.cliente_views.GuardarCambiosCliente',name='guardar_cambios_cliente'),
    url(r'^empresa/', 'modulo_1.cliente_views.RegistroEmpresaView',name='empresa_registroempresa'),
    #cargar_cliente
    url(r'^empresa_vista/', 'modulo_1.cliente_views.dt_empresas',name='dt_empresas'),
    url(r'^guardar_empresa/', 'modulo_1.cliente_views.GuardarEmpresa',name='guardar_empresa'),
    url(r'^cargar_empresa/', 'modulo_1.cliente_views.CargarEmpresa',name='cargar_empresa'),
    url(r'^guardar_cambios_empresa/', 'modulo_1.cliente_views.GuardarCambiosEmpresa',name='guardar_cambios_empresa'),

	#Usuario
	url(r'^usuario/', 'modulo_1.views.RegistroUsuarioView',name='usuario_registrousuario'),
    url(r'^usuarios_vista/', 'modulo_1.views.dt_usuarios',name='dt_usuarios'),
    url(r'^guardar_usuario/', 'modulo_1.views.GuardarUsuario',name='guardar_usuario'),
    url(r'^guardar_cambios_usuario/', 'modulo_1.views.GuardarCambiosUsuario',name='guardar_cambios_usuario'),

    #Catalogos
    url(r'^catalogos/', 'modulo_1.views.CatalogosView',name='catalogos'),
    url(r'^forma_pago/', 'modulo_1.views.dt_forma_pago',name='dt_forma_pago'),
    url(r'^forma_facturacion/', 'modulo_1.views.dt_forma_facturacion',name='dt_forma_facturacion'),
    url(r'^tipo_alquiler/', 'modulo_1.views.dt_alquiler',name='dt_alquiler'),
    url(r'^guardar_catalogo/', 'modulo_1.views.GuardarCatalogo',name='guardar_catalogo'),
    url(r'^eliminar_catalogo/', 'modulo_1.views.EliminarCatalogo',name='eliminar_catalogo'),
    url(r'^guardar_cambios_catalogo/', 'modulo_1.views.GuardarCambiosCatalogo',name='guardar_cambios_catalogo'),
    
    #Complejo
    url(r'^complejo/', 'modulo_1.datosbase_views.RegistroComplejo',name='base_registrocomplejo'),
    url(r'^dt_complejo/', 'modulo_1.datosbase_views.ComplejoData',name='dt_complejo'),
    url(r'^guardar_complejo/', 'modulo_1.datosbase_views.GuardarComplejo',name='guardar_complejo'),
    url(r'^guardar_cambios_complejo/', 'modulo_1.datosbase_views.GuardarCambiosComplejo',name='guardar_cambios_complejo'),
    url(r'^cargar_complejo/', 'modulo_1.datosbase_views.CargarComplejo',name='cargar_complejo'),
    url(r'^guardar_horario/', 'modulo_1.datosbase_views.GuardarHorario',name='guardar_horario'),
    url(r'^cargar_horario/', 'modulo_1.datosbase_views.CargarHorario',name='cargar_horario'),
    url(r'^guardar_cambios_horario/', 'modulo_1.datosbase_views.GuardarCambiosHorario',name='guardar_cambios_horario'),
    url(r'^eliminar_horario/', 'modulo_1.datosbase_views.EliminarHorarioCancha',name='eliminar_horario'),
    url(r'^dt_horario/', 'modulo_1.datosbase_views.HorarioComplejoData',name='dt_horario'),
    #Cancha
    url(r'^dt_cancha/', 'modulo_1.datosbase_views.CanchaData',name='dt_cancha'),
    url(r'^guardar_cancha/', 'modulo_1.datosbase_views.GuardarCancha',name='guardar_cancha'),
    url(r'^guardar_cambios_cancha/', 'modulo_1.datosbase_views.GuardarCambiosCancha',name='guardar_cambios_cancha'),
    url(r'^cargar_cancha/', 'modulo_1.datosbase_views.CargarCancha',name='cargar_cancha'),
    #eliminar_cancha
    url(r'^eliminar_cancha/', 'modulo_1.datosbase_views.EliminarCancha',name='eliminar_cancha'),

    #Reservas
    url(r'^reservas/', 'modulo_1.views.ReservasView',name='reservas'),
    url(r'^dt_eventos/', 'modulo_1.views.dt_eventos',name='dt_eventos'),
    url(r'^cargar_combos/', 'modulo_1.views.CargarCombos',name='cargar_combos'),
    url(r'^info_evento/', 'modulo_1.views.InformacionEvento',name='info_evento'),
    url(r'^clientes_autocomplete/', 'modulo_1.views.ClientesAutocomplete',name='clientes_autocomplete'),
    url(r'^guardar_evento/', 'modulo_1.views.GuardarEvento',name='guardar_evento'),
    url(r'^guardar_cambios_evento/', 'modulo_1.views.GuardarCambiosEvento',name='guardar_cambios_evento'),
    ]
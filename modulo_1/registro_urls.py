from django.conf.urls import include, url
from django.contrib import admin
from modulo_1 import cliente_views

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
    ]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.indice, name="indice"),
    path("perfil/", views.register, name="perfil"),
    path("registro/", views.register, name="registro"),
    path("misdatos/", views.misdatos, name="misdatos"),
    path("editar/", views.update_profile, name="update_profile"),
    
    #Admin
    path("acciones/", views.accion_list, name="accion_list"),
    path("acciones/crear/", views.create_acciones, name="create_acciones"),
    path("acciones/editar/<int:accion_id>/", views.edit_acciones, name="edit_acciones"),
    path("acciones/eliminar/<int:accion_id>/", views.delete_acciones, name="delete_acciones"),
    
    #regular  
    path("acciones/listar/", views.listar_acciones, name="listar_acciones"),
    path("acciones/comprar/<int:accion_id>/", views.comprar_accion, name="comprar_accion"),
    path("acciones/vender/<int:accion_id>/", views.vender_accion, name="vender_accion"),
    path("acciones/compradas/", views.acciones_compradas, name="acciones_compradas"),
    path('acciones/transacciones/', views.historial_transacciones, name='historial_transacciones'),
   
]
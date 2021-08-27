from django.urls import path
from . import views

app_name ="juego"
urlpatterns = [
    path('', views.listar_preguntas, name='listar_preguntas'),
    path('preguntas', views.preguntas, name="preguntas"),
    path("detalle_pregunta/<int:identificador>", views.detalle_pregunta, name="detalle_pregunta"),
    path('crear', views.crear_pregunta, name="crear_pregunta"),
    path("editar_pregunta/<int:identificador>", views.editar_pregunta, name="editar"),
    path('eliminar/<int:identificador>', views.eliminar_pregunta, name="eliminar"),
    path('confirmar_eliminacion/<int:identificador>', views.confirmar_eliminacion, name="confirmar_eliminacion"),
    path('respuestas', views.respuestas, name="respuestas"),
    path("detalle_respuesta/<int:identificador>", views.detalle_respuesta, name="detalle_respuesta"),
    path('crear_respuesta', views.crear_respuesta, name="crear_respuesta"),
    path("editar_respuesta/<int:identificador>", views.editar_respuesta, name="editar_respuesta"),
    path('eliminar_respuesta/<int:identificador>', views.eliminar_respuesta, name="eliminar_respuesta"),
    path('confirmar_eliminacionn/<int:identificador>', views.confirmar_eliminacionn, name="confirmar_eliminacionn"),
    path('categorias', views.categorias, name="categorias"),
    path("detalle_categoria/<int:identificador>", views.detalle_categoria, name="detalle_categoria"),
    path('crear_categoria', views.crear_categoria, name="crear_categoria"),
    path("editar_categoria/<int:identificador>", views.editar_categoria, name="editar_categoria"),
    path('eliminar_categoria/<int:identificador>', views.eliminar_categoria, name="eliminar_categoria"),
    path('confirmar_eliminaciion/<int:identificador>', views.confirmar_eliminaciion, name="confirmar_eliminaciion"),
    path('pagina',views.pagina),
    path('noticias',views.noticias),
    path('partidas',views.partidas, name="partidas"),
]

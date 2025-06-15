from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.registrar, name='registrar'),
    path('home/', views.home, name='home'),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.logout_view, name='logout'),
    path('subir-ejercicio/', views.up_exercise, name='subir-ejercicio'),
    path('mis-ejercicios/', views.list_my_exercises, name='listar_ejercicios'),
    path('ejercicios-comunidad/', views.list_exercises, name='ejercicios-comunidad'),
    path('agente-ejercicios/', views.exercise_agent, name='agente-ejercicios'),
    path('recuperar-contrasena/', views.recuperar_contrasena, name='recuperar-contrasena'),
    path('categorias/', views.categorias, name='categorias'),
    path('categoria_fuerza/', views.categoria_fuerza, name='categoria_fuerza'),
    path('categoria_cardio/', views.categoria_cardio, name='categoria_cardio'),
    path('categoria_flexibilidad/', views.categoria_flexibilidad, name='categoria_flexibilidad'),
    path('categoria_gluteos/', views.categoria_gluteos, name='categoria_gluteos'),
    path('categoria_espalda/', views.categoria_espalda, name='categoria_espalda'),
    path('pregunta-inteligente/', views.openAIQuestion, name='pregunta-inteligente'),
    path('comienza-entreno/', views.comienza_entreno, name='comienza-entreno'),
    path('ejercicio/<int:id>/', views.detalle_ejercicio, name='detalle-ejercicio'),
    path('editar-ejercicio/<int:id>/', views.editar_ejercicio, name='editar-ejercicio'),
    path('eliminar-ejercicio/<int:id>/', views.eliminar_ejercicio, name='eliminar-ejercicio'),
    path('mi_perfil/', views.my_profile, name='mi-perfil'),
    
    # Nivel medio
    path('categoria_gluteo_medio/', views.ejercicios_gluteo_medio, name='categoria_gluteo_medio'),
    path('categoria_espalda_medio/', views.ejercicios_espalda_medio, name='categoria_espalda_medio'),
    path('categoria_fuerza_medio/', views.ejercicios_fuerza_medio, name='categoria_fuerza_medio'),
    path('categoria_cardio_medio/', views.ejercicios_cardio_medio, name='categoria_cardio_medio'),
    path('categoria_flexibilidad_medio/', views.ejercicios_flexibilidad_medio, name='categoria_flexibilidad_medio'),

    # Nivel avanzado
    path('categoria_gluteo_alto/', views.ejercicios_gluteo_alto, name='categoria_gluteo_alto'),
    path('categoria_espalda_alto/', views.ejercicios_espalda_alto, name='categoria_espalda_alto'),
    path('categoria_fuerza_alto/', views.ejercicios_fuerza_alto, name='categoria_fuerza_alto'),
    path('categoria_cardio_alto/', views.ejercicios_cardio_alto, name='categoria_cardio_alto'),
    path('categoria_flexibilidad_alto/', views.ejercicios_flexibilidad_alto, name='categoria_flexibilidad_alto'),

    path('todos-fuerza/', views.todos_fuerza, name='todos-fuerza'),
    path('todos-cardio/', views.todos_cardio, name='todos-cardio'),
    path('todos-flex/', views.todos_flex, name='todos-flex'),
    path('todos-gluteos/', views.todos_gluteos, name='todos-gluteos'),
    path('todos-espalda/', views.todos_espalda, name='todos-espalda'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Soriana, name='inicio_soriana'),
    path('empleados/', views.ver_Empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_Empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:pk>/', views.actualizar_Empleado, name='actualizar_empleado'),
    path('empleados/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_Empleado, name='realizar_actualizacion_empleado'),
    path('empleados/borrar/<int:pk>/', views.borrar_Empleado, name='borrar_empleado'),
    
    path('clientes/', views.ver_Clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_Cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:pk>/', views.actualizar_Cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_Cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_Cliente, name='borrar_cliente'),
]


from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('estadistica/', views.estadistica, name='estadistica'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('clientes/', views.clientes, name='clientes'),
    path('proveedores/', views.proveedores, name='proveedores'),
    path('registroprov/', views.registroprov, name='registroprov'),
]
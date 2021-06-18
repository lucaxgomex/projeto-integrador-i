from django.urls import path
from .views import listar_registros, criar_registro, atualizar_registro, apagar_registro, criar_conta

urlpatterns = [
    path('', listar_registros, name='listar_registros'),
    path('novo-registro', criar_registro, name='criar_registro'),
    path('atualizar-registro/<int:id>', atualizar_registro, name='atualizar_registro'),
    path('apagar-registro/<int:id>', apagar_registro, name='apagar_registro'),
    path('criar-conta', criar_conta, name='criar_conta')
]

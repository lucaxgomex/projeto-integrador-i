from django.urls import path
#from .views import *
from . import views

app_name = 'cadastro'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home')
]

"""
urlpatterns = [
    path('', login, name='login'),
    path('listagem', listar_registros, name='listar_registros'),
    path('novo-registro', criar_registro, name='criar_registro'),
    path('atualizar-registro/<int:id>', atualizar_registro, name='atualizar_registro'),
    path('apagar-registro/<int:id>', apagar_registro, name='apagar_registro'),
    path('criar-conta', criar_conta, name='criar_conta'),
    path('test_login', test_login, name='test_login'),
]
"""

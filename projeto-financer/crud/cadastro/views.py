from django.views.generic import TemplateView
from django.urls import path, include
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Registro, Conta
from .forms import RegistroForm, ContaForm

# views relacionada aos registros
def login(request):
    return redirect('accounts/signup/')

def listar_registros(request):
    registros = Registro.objects.all()
    return render(request, 'listar_registros.html', {'registros': registros})

def criar_registro(request):
    form = RegistroForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Registro cirado com sucesso!")

        return redirect('listar_registros')
    return render(request, 'registro_form.html', {'form': form})

def atualizar_registro(request, id):
    registro = Registro.objects.get(id=id)
    form = RegistroForm(request.POST or None, instance=registro)

    if form.is_valid():
        form.save()
        messages.success(request, "Registro cirado com sucesso!")

        return redirect('listar_registros')
    return render(request, 'registro_form.html', {'form': form, 'registro': registro})

def apagar_registro(request, id):
    registro = Registro.objects.get(id=id)
    registro.delete()
    return redirect('listar_registros')

# views relacionadas as contas
def criar_conta(request):
    form = ContaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_registros')
    return render(request, 'conta_form.html', {'form': form})

def test_login(request):
    return render(request, 'test_login.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

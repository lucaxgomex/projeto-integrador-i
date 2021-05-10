from django.shortcuts import render, redirect
from .models import Registro
from .forms import RegistroForm
# Create your views here.

def listar_registros(request):
    registros = Registro.objects.all()
    return render(request, 'listar_registros.html', {'registros':registros})


def criar_registro(request):

    form = RegistroForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_registros')

    return render(request, 'registro_form.html', {'form':form})


def atualizar_registro(request, id):

    registro = Registro.objects.get(id=id)
    form = RegistroForm(request.POST or None, instance=registro) 

    if form.is_valid():
        form.save()
        return redirect('listar_registros')

    return render(request, 'registro_form.html', {'form':form, 'registro':registro} )


def apagar_registro(request, id):
    registro = Registro.objects.get(id=id)
    registro.delete()
    return redirect('listar_registros')

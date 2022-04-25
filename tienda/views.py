from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ProveedorForm
from .models import Cliente
from .models import Proveedor


# Create your views here.

def index(request):
    return render(request, 'tienda/index.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def estadistica(request):
    return render(request, 'tienda/estadistica.html')

def confirmacion(request):
    datos= request.GET
    nombre=datos["nombre"]
    email=datos["email"]
    mensaje=datos["mensaje"]
    print(nombre, email, mensaje)
    return render(request, 'tienda/confirmacion.html', {"mensaje":"Datos recibidos"})

def clientes(request):
    cliente=Cliente.objects.all().values()
    context = {
    'clientes': cliente,
    }
    return render(request, 'tienda/clientes.html', context)

def proveedores(request):
    proveedor=Proveedor.objects.all().values()
    context = {
    'proveedores': proveedor,
    }
    return render(request, 'tienda/proveedores.html', context)

def registroprov(request):

    form=ProveedorForm()

    if request.method == 'POST':
		
        form = ProveedorForm(request.POST)

        if form.is_valid():
            proveedor=Proveedor()
            proveedor.nombre=form.cleaned_data["nombre"]
            proveedor.razon_social=form.cleaned_data["razon_social"]
            proveedor.telefono=form.cleaned_data["telefono"]
            proveedor.correo_electronico=form.cleaned_data["correo_electronico"]
            proveedor.categoria=form.cleaned_data["categoria"]
            proveedor.save()
            messages.success(request, 'Los datos han sido guardados satisfactoriamente')
        else: messages.error('Inválido')
        return redirect('index')
    else:
        form=ProveedorForm() 
        return render(request, 'tienda/registroprov.html', {"form":form}) 




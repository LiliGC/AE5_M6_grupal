from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
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

@login_required
def clientes(request):
    cliente=Cliente.objects.all().values()
    context = {
    'clientes': cliente,
    }
    return render(request, 'tienda/clientes.html', context)

@login_required
def proveedores(request):
    proveedor=Proveedor.objects.all().values()
    context = {
    'proveedores': proveedor,
    }
    return render(request, 'tienda/proveedores.html', context)

@staff_member_required
@login_required
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
        else: messages.error('Inv??lido')
        return redirect('index')
    else:
        form=ProveedorForm() 
        return render(request, 'tienda/registroprov.html', {"form":form}) 


def register_user(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registro exitoso." )
			return redirect('index')
		messages.error(request, "Registro no exitoso. Informaci??n no v??lida.")
	form = NewUserForm()
	return render (request, 'tienda/register_user.html', context={"register_form":form})


def login_user(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Tu haz iniciado sesi??n como {username}.")
				return redirect('login')
			else:
				messages.error(request,"Nombre o contrase??a no v??lidos.")
		else:
			messages.error(request,"Nombre o contrase??a no v??lidos.")
	form = AuthenticationForm()
	return render(request, 'tienda/login.html',context={"login_form":form})

@login_required
def logout_user(request):
	logout(request)
	messages.info(request, "Haz cerrado sesi??n exitosamente.") 
	return redirect('index')




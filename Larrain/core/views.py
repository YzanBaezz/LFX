from django.shortcuts import render, redirect
from . import views
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Producto,Servicio

# Create your views here.



def login(request):

    return render(request, 'core/login.html')

def RegistroHora(request):
    return render(request, 'core/RegistroHora.html')

def Servicios(request):
    Productos = Producto.objects.all()
    Servicios = Servicio.objects.all()
    contexto = {
        "Productos" : Productos,
        "Servicios" : Servicios
    }
    return render(request, 'core/Servicios.html',contexto)

def producto(request):
    return render(request, 'core/producto.html')

def producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    contexto = {
        "produc" : producto,
    }
    return render(request,'core/producto.html',contexto)

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()

    contexto = {'form': form}
    return render(request, 'core/registro.html', contexto)

def index(request):
    Productos = Producto.objects.all()
    numero = 2
    contexto = {
        "Productos" : Productos,
        "numero" : numero ,
    }
    return render(request,'core/index.html',contexto)

def logout(request):

    return render(request, 'core/logout.html')
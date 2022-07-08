from django.shortcuts import render, redirect
from . import views
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Producto

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def login(request):

    return render(request, 'core/login.html')

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


def logout(request):

    return render(request, 'core/logout.html')
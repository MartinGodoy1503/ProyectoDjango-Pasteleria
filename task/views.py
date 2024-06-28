from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import CustomUser, Producto
from .forms import CustomAuthenticationForm, CustomUserCreationForm, ProductoForm
from django.contrib.auth import login as auth_login, authenticate,  logout as auth_logout

# Create your views here.

def home (request):
    return render(request, 'home.html')

#VISTA PARA CREAR UN USUARIO 

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            correo_electronico = form.cleaned_data['correo_electronico']
            password1 = form.cleaned_data['password1']
            id_genero = form.cleaned_data['id_genero']
            id_estado = form.cleaned_data['id_estado']

            if password1 != form.cleaned_data['password2']:
                context = {
                    'form': form,
                    'username': username,
                    'password_error': "Las contraseñas no coinciden."
                }
                return render(request, 'signup.html', context)

            try:
                user = form.save(commit=False)
                user.set_password(password1)
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                context = {
                    'form': form,
                    'username': username,
                    'username_error': "El usuario ya existe."
                }
                return render(request, 'signup.html', context)

    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

#LOGIN USUARIO CUSTOM
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Bienvenido, {user.username}")
                return redirect('home')
            else:
                messages.error(request, "Correo electrónico o contraseña incorrectos.")
        else:
            messages.error(request, "Correo electrónico o contraseña incorrectos.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('login')



# VISTAS CRUD PARA EL MODELO (TABLA) PRODUCTO
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detail.html', {'producto': producto})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'producto_form.html', {'form': form, 'action': 'create'})

def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_form.html', {'form': form, 'action': 'edit'})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'producto_confirm_delete.html', {'producto': producto})
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login
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
            print("Formulario válido, guardando usuario...")
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            try:
                user.save()
                login(request, user)
                print("Usuario guardado correctamente, redirigiendo...")
                return redirect('home')  # Redirige a la página de inicio después del registro exitoso
            except IntegrityError:
                form.add_error('correo_electronico', "El correo electrónico ya está en uso.")
                print("Error de integridad al guardar el usuario.")
        else:
            print("Formulario inválido:", form.errors)
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
                print(f"Inicio de sesión exitoso para usuario: {user.username}")
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
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout, authenticate
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

#VISTA EN DESHUSO 

def tasks (request):
    return render(request, 'tasks.html')   


#VISTA PARA MENSAJE DE CONTACTO SUCCESSFULLY 
def success (request):
    return render(request, 'success.html')

def signout(request):
    logout(request)
    return redirect('home')

#VISTA PARA INGRESAR CON USUARIO EXISTENTE 
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'El usuario o Contraseña no es válido/a'
            })
        else:
            login(request, user)    
            return redirect('home')

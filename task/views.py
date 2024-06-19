from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home (request):
    return render(request, 'home.html')

#VISTA PARA CREAR UN USUARIO 

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "El usuario ya existe."})
            
        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Contraseñas no coinciden."})

#VISTA EN DESHUSO 

def tasks (request):
    return render(request, 'tasks.html')   

#VISTA PARA LA CREACION DE UN FORMULARIO DE CONTACTO

@login_required
def create_contact(request):
    if request.method == 'GET':
        return render(request, 'create_contact.html', {'form': ContactForm()})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            try:
                contact.save()
                return redirect('success_page')
            except IntegrityError:
                form.add_error(None, 'Error al guardar el formulario. Inténtalo de nuevo.')
        return render(request, 'create_contact.html', {'form': form})
      


#VISTA PARA MENSAJE DE CONTACTO SUCCESSFULLY 
def success (request):
    return render(request, 'success.html')

def signout(request):
    logout(request)
    return redirect('home')

#VISTA PARA INGRESAR CON USUARIO EXISTENTE 
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'El usuario o Contraseña no es válido/a'
                })
        else:
            login(request, user)    
            return redirect ('home')

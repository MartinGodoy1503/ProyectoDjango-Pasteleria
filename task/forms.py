from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, GeneroCliente, Producto


# ---------------------------FORMULARIOS ------------------------------------------ 

# CREACION DE USUARIOS CUSTOM, CREACION DE SUPERUSUARIO
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('nombre_usuario', 'correo_electronico', 'id_genero', 'id_estado')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_genero'].queryset = GeneroCliente.objects.all()

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('nombre_usuario', 'correo_electronico', 'id_genero', 'id_estado')

#INICIO DE SESION CON EL USUARIO
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Correo Electrónico', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


#PRODUCTO
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion', 'precio', 'stock', 'id_categoria'] 

#VALIDACIONES DIRECTAMENTE DESDE FORMS        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['descripcion', 'precio', 'stock']

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion:
            raise forms.ValidationError('Este campo es obligatorio.')
        if len(descripcion) < 5:
            raise forms.ValidationError('La descripción debe tener al menos 5 caracteres.')
        return descripcion

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor que cero.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo.')
        return stock
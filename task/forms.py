from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, GeneroCliente

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'correo_electronico', 'id_genero', 'id_estado')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_genero'].queryset = GeneroCliente.objects.all()
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'nombre_usuario', 'correo_electronico', 'id_genero', 'id_estado')
        
        
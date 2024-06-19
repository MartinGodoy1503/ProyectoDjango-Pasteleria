from django.forms import ModelForm

# app_name/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nombre', 'email', 'celular', 'mensaje']
    
    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        words = mensaje.split()
        if len(words) < 10:
            raise forms.ValidationError('El mensaje debe tener al menos 10 palabras.')
        return mensaje

    def clean_celular(self):
        celular = self.cleaned_data.get('celular')
        if not celular.startswith('9') or len(celular) != 9:
            raise forms.ValidationError('El número de celular no es válido.')
        return celular


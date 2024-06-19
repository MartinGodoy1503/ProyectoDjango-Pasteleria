from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    celular = models.CharField(max_length=10)
    mensaje = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre + ' - ' + self.user.username
    
    
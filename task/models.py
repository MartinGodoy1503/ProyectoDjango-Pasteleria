from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator


class GeneroCliente(models.Model):
    id_genero = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class CategoriaProducto(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.descripcion


class CustomUserManager(BaseUserManager):
    def create_user(self, correo_electronico, password=None, **extra_fields):
        if not correo_electronico:
            raise ValueError('El campo de correo electrónico debe ser establecido')
        correo_electronico = self.normalize_email(correo_electronico)
        user = self.model(correo_electronico=correo_electronico, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo_electronico, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('username', correo_electronico) 
        return self.create_user(correo_electronico, password, **extra_fields)

    def get_by_natural_key(self, correo_electronico):
        return self.get(correo_electronico=correo_electronico)


class CustomUser(AbstractUser):
    nombre_usuario = models.CharField(max_length=50, unique=True)
    correo_electronico = models.EmailField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_genero = models.ForeignKey(GeneroCliente, on_delete=models.SET_NULL, null=True, blank=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.nombre_usuario


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.descripcion


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    fecha_pedido = models.DateField()
    estado_pedido = models.CharField(max_length=20, default='pendiente')
    id_cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'Pedido {self.id_pedido}'

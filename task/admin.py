from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CategoriaProducto, CustomUser, Estado, GeneroCliente, Pedido, Producto


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('nombre_usuario', 'correo_electronico', 'id_genero', 'id_estado')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'correo_electronico', 'password1', 'password2', 'id_genero', 'id_estado', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('username', 'correo_electronico', 'nombre_usuario', 'id_genero', 'id_estado', 'is_staff', 'is_superuser')
    search_fields = ('username', 'correo_electronico', 'nombre_usuario')
    ordering = ('username',)

# Registra los modelos en el admin
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(GeneroCliente)
admin.site.register(Estado)
admin.site.register(CategoriaProducto)
admin.site.register(Producto)
admin.site.register(Pedido)

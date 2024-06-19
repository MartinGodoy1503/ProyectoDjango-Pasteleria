from django.contrib import admin
from .models import Contact
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("creacion", )

admin.site.register(Contact, TaskAdmin)

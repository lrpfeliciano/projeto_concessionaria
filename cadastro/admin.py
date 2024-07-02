from django.contrib import admin

from cadastro.models import Cliente, Marca, Modelo 


# Register your models here.
admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Modelo)

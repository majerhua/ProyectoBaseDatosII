from django.contrib import admin

# Register your models here.

from .models import Proyecto
from .models import ProyectoDocs


admin.site.register(Proyecto)
admin.site.register(ProyectoDocs)
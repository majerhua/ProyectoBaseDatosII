from django.contrib import admin

# Register your models here.

from .models import Proyecto


from .models import ProyectoDocs



from .models import Distrito
from .models import Provincia
from .models import Departamento
from .models import Cliente


admin.site.register(Cliente)
admin.site.register(ProyectoDocs)
admin.site.register(Proyecto)
admin.site.register(Departamento)
admin.site.register(Distrito)
admin.site.register(Provincia)


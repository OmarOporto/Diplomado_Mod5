from django.contrib import admin
from .models import Categoria
from .models import cells
from .models import guards

"""
Categoria
"""
admin.site.register(Categoria)

"""


Cells
"""
class CellsAdmin(admin.ModelAdmin):
    list_display = ("number_id","number_beds","revision","size")
    search_fields = ["number_id"]

admin.site.register(cells, CellsAdmin)
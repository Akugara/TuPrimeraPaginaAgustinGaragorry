from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    filter_horizontal = ('estudiantes',)  # or filter_vertical

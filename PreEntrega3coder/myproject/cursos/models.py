from django.db import models
from profesores.models import Profesor
from estudiantes.models import Estudiante

class Curso(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name='taught_courses')
    estudiantes = models.ManyToManyField(Estudiante, related_name='enrolled_courses')
    
    def __str__(self):
        return self.title

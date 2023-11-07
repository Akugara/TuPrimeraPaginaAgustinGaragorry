from django.db import models

class Estudiante(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    grades = models.JSONField(default=dict)  
    
    def __str__(self):
        return self.name
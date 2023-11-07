from django.db import models

class Profesor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    course = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
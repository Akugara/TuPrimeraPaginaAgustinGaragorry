from django.shortcuts import render
from profesores.models import Profesor
from estudiantes.models import Estudiante
# Import other necessary modules...

def home(request):
    return render(request, 'home.html')

def search_results(request):
    name_query = request.GET.get('name', '')
    surname_query = request.GET.get('surname', '')
    
    estudiantes = Estudiante.objects.filter(name__icontains=name_query, surname__icontains=surname_query)
    profesores = Profesor.objects.filter(name__icontains=name_query, surname__icontains=surname_query)
    
    return render(request, 'search_results.html', {
        'estudiantes': estudiantes,
        'profesores': profesores
    })

# Your other view functions...

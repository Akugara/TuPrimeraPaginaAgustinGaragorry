from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteRegistrationForm

def estudiante_list(request):
    estudiantes = Estudiante.objects.all()  # Retrieve all estudiantes from the database
    context = {
        'estudiantes': estudiantes
    }
    return render(request, 'estudiantes/estudiantes_list.html', context)

def register_estudiante(request):
    if request.method == 'POST':
        form = EstudianteRegistrationForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)
            estudiante.save()  # Save the Estudiante instance
            for curso in form.cleaned_data['enrolled_courses']:
                estudiante.enrolled_courses.add(curso)
            return redirect('estudiantes:estudiante_list')
    else:
        form = EstudianteRegistrationForm()
    return render(request, 'estudiantes/register_estudiante.html', {'form': form})






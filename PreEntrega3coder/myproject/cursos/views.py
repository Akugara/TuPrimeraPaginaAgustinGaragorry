from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from .forms import CursoForm
from .models import Curso

def curso_list(request):
    cursos = Curso.objects.all()
    context = {
        'cursos': cursos
    }
    return render(request, 'cursos/cursos_list.html', context)

def create_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos:curso_list')  
    else:
        form = CursoForm()  # This line should be inside the else block
    return render(request, 'cursos/create_curso.html', {'form': form})


def course_detail(request, course_id):
    curso = get_object_or_404(Curso, pk=course_id)
    estudiantes = curso.estudiantes.all()
    context = {
        'curso': curso,
        'estudiantes': estudiantes,
    }
    return render(request, 'cursos/course_detail.html', context)


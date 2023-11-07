
from django.shortcuts import render, redirect
from .models import Profesor
from .forms import ProfesorForm


def index(request):  # Changed from profesor_list to index
    profesores = Profesor.objects.all()
    context = {
        'profesores': profesores
    }
    return render(request, 'profesores/profesores_list.html', context)

def register_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores:profesor_list')
    else:
        form = ProfesorForm()
    return render(request, 'profesores/register_profesor.html', {'form': form})
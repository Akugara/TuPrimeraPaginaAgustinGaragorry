from django import forms
from .models import Curso
from profesores.models import Profesor

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['title', 'code', 'profesor']
        labels = {
            'title': 'Materia',
            'code': 'Código',
            'profesor': 'Profesor',
        }
        widgets = {
            'profesor': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CursoForm, self).__init__(*args, **kwargs)
        self.fields['profesor'].queryset = Profesor.objects.all()
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['code'].widget.attrs.update({'class': 'form-control'})

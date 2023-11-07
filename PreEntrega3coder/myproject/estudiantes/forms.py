from django import forms
from .models import Estudiante
from cursos.models import Curso


class EstudianteRegistrationForm(forms.ModelForm):
    enrolled_courses = forms.ModelMultipleChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'enrolled-courses'}),
        required=False,
        help_text='Selecciona el curso al que se inscribirá el estudiante'
    )
    
    class Meta:
        model = Estudiante
        fields = ['name', 'surname', 'age', 'gender', 'enrolled_courses']

    def __init__(self, *args, **kwargs):
        super(EstudianteRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control'})
        self.fields['age'].widget.attrs.update({'class': 'form-control'})
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
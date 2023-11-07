from django.urls import path
from .views import estudiante_list, register_estudiante

app_name = 'estudiantes'

urlpatterns = [
    path('', estudiante_list, name='estudiante_list'),
    path('register/', register_estudiante, name='register_estudiante'),

]

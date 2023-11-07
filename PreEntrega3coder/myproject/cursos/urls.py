from django.urls import path
from .views import curso_list, create_curso, course_detail

app_name = 'cursos'

urlpatterns = [
    path('', curso_list, name='curso_list'),
    path('create/', create_curso, name='create_curso'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),

]

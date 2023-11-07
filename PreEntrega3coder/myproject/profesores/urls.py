from django.urls import path
from . import views
from .views import register_profesor

app_name = 'profesores'  # This is the namespace

urlpatterns = [
    path('', views.index, name='profesor_list'),  # The 'name' here should match the one used in the template
    path('register/', register_profesor, name='register_profesor'),

    # ... other URL patterns ...
]

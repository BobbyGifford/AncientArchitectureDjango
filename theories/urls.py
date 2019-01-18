from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='theories'),
    path('<int:theory_id>', views.theory, name='theory')
]

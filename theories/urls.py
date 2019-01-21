from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='theories'),
    path('<int:theory_id>', views.theory, name='theory'),
    path('add_theory', views.add_theory, name='add_theory'),
    path('edit_theory/<int:theory_id>', views.edit_theory, name='edit_theory'),
    path('delete_theory/<int:theory_id>', views.delete_theory, name='delete_theory')
]

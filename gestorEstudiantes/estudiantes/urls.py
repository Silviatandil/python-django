from django.urls import path
from . import views

urlpatterns=[
    path('',views.mostrar_estudiante),
    path('create/<str:nombre>/<str:apellido>/<int:edad>/<int:nota>',views.crear_estudiantes),
    path('filter/<int:nota>', views.filtrar_estudiante_nota),
    path('update/<int:id>/<str:nombre>/<str:apellido>/<int:edad>/<int:nota>', views.update_estudiante_id),
    path('delete/<int:id>', views.borrar_estudiante_id),
    path('delete', views.borrar_estudiante)

]
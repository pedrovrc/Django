from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name='registrar'),
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('nova/', views.nova_tarefa, name='nova_tarefa'),
    path('<int:id>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('<int:id>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
    path('<int:id>/concluir/', views.concluir_tarefa, name='concluir_tarefa'),
]
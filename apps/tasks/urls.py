from django.urls import path
from .views import *

app_name = 'tasks'

urlpatterns = [
    #categorias
    path('categoria/listagem/',
        list_category,
        name='list_categories'
    ),
    path('categoria/adicionar/',
        add_category,
        name='add_category'
    ),
    path('categoria/editar/<int:id_category>/',
        edit_category,
        name='edit_category'
    ),
    path('categoria/excluir/<int:id_category>/',
        delete_category,
        name='delete_category'
    ),
    #tarefas
    path('tarefa/listagem/',
        list_tasks,
        name='list_tasks'
    ),
    path('tarefa/adicionar/', 
        add_tasks, 
        name='add_tasks'
    ),
    path('tarefa/editar/<int:id_task>/',
        edit_tasks,
        name='edit_tasks'
    ),
    path('tarefa/excluir/<int:id_tasks>/',
        delete_tasks,
        name='delete_tasks'
    ),
]

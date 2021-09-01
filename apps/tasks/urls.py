from django.urls import path
from .views import *


app_name = 'tasks'

urlpatterns = [
    path('adicionar/',
        add_category,
        name='add_category'
    ),
    path('editar/<int:id_category>/',
        edit_category,
        name='edit_category'
    ),
    path('',
        list_category,
        name='list_categories'
    ),
]

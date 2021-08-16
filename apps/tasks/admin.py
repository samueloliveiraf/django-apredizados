from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'descripition',
        'ower',
    ]

class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'descripition',
        'priority',
        'end_date',
        'status',
    ]

admin.site.register(
    Category, 
    CategoryAdmin,
)

admin.site.register(
    Task,
    TaskAdmin,
)


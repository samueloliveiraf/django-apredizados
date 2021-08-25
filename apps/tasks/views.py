from django.shortcuts import render
from django.contrib import messages
from .forms import *


def add_category(request):
    template_name = 'tasks/add_category.html'
    context = {}

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ower = request.user
            f.save()
            messages.success(request, 'Adicionado com sucesso!')

    form = CategoryForm()
    context['form'] = form
    
    return render(request, template_name, context)


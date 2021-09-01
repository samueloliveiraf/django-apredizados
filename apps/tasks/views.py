from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .forms import *
from .models import *


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


def list_category(request):
    template_name = 'tasks/list_categories.html'
    categories = Category.objects.filter(
        ower=request.user
    )
    
    context = {
        'categories': categories
    }

    return render(request, template_name, context)


def edit_category(request, id_category):
    template_name = 'tasks/add_category.html'
    context = {}
    category = get_object_or_404(
        Category, 
        id=id_category, 
        ower=request.user
    )

    if request.method == 'POST':
        form = CategoryForm(
            request.POST, 
            instance=category
        )
        if form.is_valid():
            form.save()

            return redirect('category:list_categories')
    
    form = CategoryForm(instance=category)
    context['form'] = form
    
    return render(request, template_name, context)


def delete_category(request, id_category):
    category = Category.objects.get(id=id_category)
    if category.ower == request.user:
        category.delete()
    else:
        messages.error(request, 'Você não tem permição para excluir')
        return redirect('core:home')
    
    return redirect('category:list_categories')


def add_tasks(request):
    template_name = 'tasks/add_taks.html'
    context = {}

    if request.method == 'POST':
        form =TaskForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ower = request.user
            f.save()
            form.save_m2m()
            messages.success(request, 'Adicionado com sucesso!')
        else:
            print(form.errors)
            
    form = TaskForm()
    context['form'] = form
    
    return render(request, template_name, context)


def list_tasks(request):
    template_name = 'tasks/list_tasks.html'
    tasks = Task.objects.filter(
        ower=request.user
    )
    
    context = {
        'tasks': tasks
    }

    return render(request, template_name, context)


def edit_tasks(request, id_task):
    template_name = 'tasks/add_taks.html'
    context = {}
    task = get_object_or_404(
        Task, 
        id=id_task, 
        ower=request.user
    )

    if request.method == 'POST':
        form = TaskForm(
            request.POST, 
            instance=task
        )
        if form.is_valid():
            form.save()

            return redirect('tasks:list_tasks')
    
    form = TaskForm(instance=task)
    context['form'] = form
    
    return render(request, template_name, context)


def delete_tasks(request, id_tasks):
    tasks = Task.objects.get(id=id_tasks)
    if tasks.ower == request.user:
        tasks.delete()
    else:
        messages.error(request, 'Você não tem permição para excluir')
        return redirect('core:home')
    
    return redirect('tasks:list_tasks')

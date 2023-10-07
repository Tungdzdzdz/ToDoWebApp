from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import TaskForm
from .models import Task


def home(request, page):
    if request.user.is_authenticated:
        tasks = Task.objects.all().filter(user=request.user)
        paginator = Paginator(tasks, per_page=10)
        page_object = paginator.get_page(page)
        page_object.adjusted_elided_pages = paginator.get_elided_page_range(page, on_ends=1, on_each_side=1)
        previous_page = page-1 if page > 2 else 1
        next_page = page+1
        return render(request, 'todo/home.html', {'tasks': page_object, 'title_site': 'Home', 'page': page})
    return redirect('login')


@login_required
def create(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'todo/update.html', {'form': form, 'title_site': 'Create'})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home', page=1)
        return render(request, 'todo/update.html', {'form': form, 'title_site': 'Create'})


@login_required
def update(request, id):
    task = get_object_or_404(Task, id=id)
    if task.user == request.user:
        if request.method == 'GET':
            form = TaskForm(instance=task)
            return render(request, 'todo/update.html', {'form': form, 'title_site': 'Update'})
        elif request.method == 'POST':
            if 'delete' in request.POST:
                task.delete()
                return redirect('home', page=1)
            elif 'save' in request.POST:
                form = TaskForm(request.POST, instance=task)
                if form.is_valid():
                    form.save()
                    return redirect('home', page=1)
                return render(request, 'todo/update.html', {'form': form, 'title_site': 'Update'})
    return redirect('home', page=1)

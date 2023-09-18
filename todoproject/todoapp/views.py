from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'data'


class Taskdetailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'taskdetail'


class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'updatetask'
    fields = ('task_name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cvdetail', kwargs={'pk': self.object.id})


class Taskdeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cvhome')


# Create your views here.


def home(request):
    data = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(task_name=name, priority=priority, date=date)
        task.save()
    return render(request, 'home.html', {'data': data})


def delete_task(request, task_id):
    del_task = Task.objects.get(id=task_id)
    if request.method == "POST":
        del_task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, task_id):
    tasks = Task.objects.get(id=task_id)
    edit_task = TodoForm(request.POST or None, instance=tasks)
    if edit_task.is_valid():
        edit_task.save()
        return redirect('/')
    return render(request, 'edit.html', {'tasks': tasks, 'edit_task': edit_task})

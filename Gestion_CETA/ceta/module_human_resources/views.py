# module_human_resources/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Worker
#from ceta.forms import WorkerForm, CategoryForm

"""
def index(request):
    return render(request, "ceta/index.html", {
        "workers" : 
    })
"""

def list_workers(request):
    return render(request, 'ceta/templates/human_resources/list_workers.html')

"""
def worker_get(request, id_w):
    if id_w > 0:
        workers = get_object_or_404(Worker, id_w=id_w)
    else:
        workers = Worker.objects.all()
    return render(request, 'ceta/templates/human_resources/list_workers.html', {'worker': workers})

def worker_create(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_workers')
    else:
        form = WorkerForm()
    return render(request, 'ceta/templates/human_resources/worker_form.html', {'form': form})

def worker_update(request, id_w):
    worker = get_object_or_404(Worker, id_w=id_w)
    if request.method == 'POST':
        form = WorkerForm(request.POST, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('list_workers')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'ceta/templates/human_resources/worker_form.html', {'form': form})

def worker_delete(request, id_w):
    worker = get_object_or_404(Worker, id_w=id_w)
    if request.method == 'POST':
        worker.delete()
        return redirect('worker_list')
    return render(request, 'ceta/templates/human_resources/worker_confirm_delete.html', {'worker': worker})
"""
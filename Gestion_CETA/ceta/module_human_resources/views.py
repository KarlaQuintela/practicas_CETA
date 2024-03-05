from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Worker

# Create your views here.
#Mostrar trabajadores
def list_workers(request):
    return render(request,'list_workers.html')  

#CRUD Worker
class WorkerList(ListView):
    model = Worker

class WorkerDetail(DetailView):
    model = Worker

class WorkerCreate(CreateView):
    model = Worker
    fields = '__all__'  # Use all fields from the model
    success_url = '/workers/'  # Redirect after successful creation

class WorkerUpdate(UpdateView):
    model = Worker
    fields = '__all__'
    success_url = '/workers/'

class WorkerDelete(DeleteView):
    model = Worker
    success_url = '/workers/'

#_________________________________________________________________________________
#CRUD Category
class CategoryList(ListView):
    model = Category

class CategoryDetail(DetailView):
    model = Category

class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/categories/'

class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/categories/'

class CategoryDelete(DeleteView):
    model = Category
    success_url = '/categories/'

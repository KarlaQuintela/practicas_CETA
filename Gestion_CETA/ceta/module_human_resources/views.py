# module_human_resources/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Worker


def list_workers(request):
    return render(request, 'html/indexTrabajador.html',{
        "workers": Worker.objects.all()
    })


def get_worker(request, id_worker):
    worker = Worker.objects.get(pk=id_worker)
    return render(request, "html/trabajadorDetalle.html",{
        "worker": worker
    })


from django.urls import path
from .module_human_resources import views

urlpatterns = [
    path('',  views.list_workers, name="index"),
    path("<int:id_worker>", views.get_worker, name="worker"),
]

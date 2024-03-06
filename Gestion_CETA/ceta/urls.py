from django.urls import path
from .module_human_resources import views

urlpatterns = [
    path('',  views.list_workers, name="indexTrabajador"),
    path("<int:id_worker>", views.get_worker, name="workerDetail"),

    # trabajadores
    path('workers/<int:id>', worker_view.as_view(), name='w_process'),
    path('workers/post/', worker_view.as_view(), name='post_w'),
    path('workers/put/<int:id>', worker_view.as_view(), name='w_update'),    
    path('workers/delete/<int:id>', worker_view.as_view(), name='delete_w'),
    
]

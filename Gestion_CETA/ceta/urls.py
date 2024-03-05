from django.urls import path
from .module_human_resources.views import list_workers

urlpatterns = [
   path('', list_workers)
]

 
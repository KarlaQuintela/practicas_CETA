from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .module_human_resources.views import *

urlpatterns = [    
    path('api-token-auth/', obtain_auth_token), #access to token auth
]

""" 
path('workers/<int:id>', worker_view.as_view(), name='w_process'),
path('workers/post/', worker_view.as_view(), name='post_w'),
path('workers/put/<int:id>', worker_view.as_view(), name='w_update'),    
path('workers/delete/<int:id>', worker_view.as_view(), name='delete_w'),
"""
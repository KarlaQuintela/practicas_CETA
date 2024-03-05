from django.shortcuts import render

# Create your views here.
def list_workers(request):
    return render(request,'list_workers.html')

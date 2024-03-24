# module_human_resources/views.py
import json
from django.core import serializers
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import GenericAPIView

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Worker

class worker_view(GenericAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # id = 0 para que devuelva todos los trabajadores, si id!=0 entonces va a devolver el trabajador cuyo id es igual
    # al valor
    def get(self, request, id):
        if id > 0:
            workers = list(Worker.objects.filter(pk=id).all())
            workers_json = serializers.serialize('json', workers)
            if len(workers) > 0:
                data = {'message': "Trabajador Cargado", 'trabajador': workers_json}
            else:
                data = {'message': "Trabajador no encontrado..."}
            return JsonResponse(data)
        else:
            workers = Worker.objects.all()
            workers_json = serializers.serialize('json', workers)

            if len(workers) > 0:
                data = {'message': "Todos los trabajadores cargados", 'trabajadores': workers_json}
            else:
                data = {'message': "Trabajadores no encontrados..."}
            return JsonResponse(data)

    def post(self, request):
        # Obtener los datos del request
        data = json.loads(request.body)
        id_w = data.get('id_worker')
        name_w = data.get('name')  
        category = data.get('category') 
        address_w = data.get('address') 
        phone_w = data.get('phone') 
        email_w = data.get('email') 
        department_w = data.get('department') 
        num_account_w =data.get('num_account')        
       
        new_w = None  # Define nuevo_trabajador con un valor predeterminado
        try:
            fk_id_cg = Category.objects.get(pk=category) # Obtener una instancia válida del modelo categoria
            new_w = Worker.objects.create(id_w=id_w, name_w=name_w, fk_id_cg=fk_id_cg, address_w=address_w, 
            phone_w=phone_w, email_w=email_w, department_w=department_w, num_account_w=num_account_w)

        except Category.DoesNotExist:
            data = {'message': "La categoría especificada no existe"}

            # Guardar el objeto en la base de datos
            new_w.save()

        # Crear una respuesta en JSON
        response_data = {
            'mensaje': 'Trabajador creado exitosamente'
        }
        return JsonResponse(response_data)

    
    def put(self, request, id):
        jd = json.loads(request.body)
        id_w = jd.get('id_worker')
        name_w = jd.get('name')  
        category = jd.get('category') 
        address_w = jd.get('address') 
        phone_w = jd.get('phone') 
        email_w = jd.get('email') 
        department_w = jd.get('department') 
        num_account_w =jd.get('num_account')      
       
        worker = list(Worker.objects.filter(pk=id).values())
        if len(worker) > 0:
            worker_aux = Worker.objects.get(pk=id)
            worker_aux.name_w = name_w
            worker_aux.id_w = id_w            
            worker_aux.address_w=address_w
            worker_aux.phone_w=phone_w
            worker_aux.email_w=email_w
            worker_aux.department_w=department_w
            worker_aux.num_account_w=num_account_w         
            
            fk_id_cg = Category.objects.get(pk=category)
            worker_aux.fk_id_cg=fk_id_cg

            worker_aux.save()
            data = {'message': "Trabajador actualizado con exito"}
        else:
            data = {'message': "Trabajador no encontrado"}
        return JsonResponse(data)

    def delete(self, request, id):
        # obtener el trabajador por su id
        try:
            worker = Worker.objects.get(pk=id)
        except Worker.DoesNotExist:
            # si el trabajador no existe, devolver error 404
            data = {'error': 'Trabajador no encontrado'}
            return JsonResponse(data, status=404)
        # eliminar el trabajador si lo encuentra
        worker.delete()
        data = {'message': 'Trabajador eliminado'}
        return JsonResponse(data)


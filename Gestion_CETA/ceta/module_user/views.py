# users/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

from ceta.forms import RoleForm
from .models import User, Role

class Role_view(): 
    def POST(request):
        if request.method == 'POST':
            form = RoleForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('role')

"""
class Role_view(GenericAPIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #GET: Recuperar información.
    def GET(self, request, id=0):
        if id > 0:
            roles = list(Role.objects.filter(id=id).values())
            if len(roles) > 0:
                data = {'message': "Rol cargado", 'roles': roles}
            else:
                data = {'message': "Rol no encontrado..."}
            return JsonResponse(data)
        else:
            roles = list(Role.objects.values())
            if len(roles) > 0:
                data = {'message': "Todos los roles cargado", 'roles': roles}
            else:
                data = {'message': "Roles no encontrados..."}
            return JsonResponse(data)

    #POST: Enviar datos al servidor (crear).
    def POST(self, request):
        jd = json.loads(request.body)
        name_role = jd['name_role']
        description_role = jd['description_role']

        if name_role == "":
            data = {'message': "Error, nombre vacío"}
        else:
            Role.objects.create(name_role = jd['name_role'])
            data = {'message': "Rol creado"}
        return JsonResponse(data)

    #PUT: Actualizar un recurso existente.
    def put(self, request, id):

        jd = json.loads(request.body)
        roles = list(rol.objects.filter(id=id).values())

        if len(roles) > 0:
            rol_aux = rol.objects.get(id=id)
            rol_aux.nombre_rol = jd['nombre_rol']

            rol_aux.save()
            data = {'message': "Rol actualizado"}
        else:
            data = {'message': "Rol no encontrado..."}
        return JsonResponse(data)

    #DELETE: Eliminar un recurso.
    def delete(self, request, id):
        roles = list(rol.objects.filter(id=id).values())

        if len(roles) > 0:
            rol.objects.filter(id=id).delete()
            data = {'message': "Rol eliminado"}
        else:
            data = {'message': "Rol no encontrado..."}
        return JsonResponse(data)
"""
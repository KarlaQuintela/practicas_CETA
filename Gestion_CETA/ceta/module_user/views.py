# module_user/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from serializers import UserSerializer,RoleSerializer

from django.shortcuts import render, redirect,get_object_or_404

from .models import User, Role

@api_view(['GET'])
def login(request):
    user = get_object_or_404(User,username=request.data['username'])
    response = Response({})
    if not user.check_password(request.data['password']):
        response = Response({'error': 'invalid password'},status=status.HTTP_400_BAD_REQUEST)
    else:
        token,created = Token.objects.get_or_create(user=user)
        serialized_user = UserSerializer(instance=user)
        response = Response({
            'token': token.key, 
            "user": serialized_user.data
        },status=status.HTTP_200_OK)
    return response
@api_view(['POST'])
def sign_in(request):
    #TODO add role
    # role = Role.objects.filter(name_role=request.data.role).get('id_role')
    # request_data: dict = {}
    user_data = UserSerializer(data=request.data)
    response = Response({user_data.errors},status=status.HTTP_400_BAD_REQUEST)
    if(user_data.is_valid()):
        user_data.save()
        user = User.objects.get(username=user_data.data['username'])
        user.set_password(user_data.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        response.data = {
        'token': token.key,
        "user": user_data.data
        }
        response.status_code = status.HTTP_201_CREATED
    return response

"""

class Role_view(): 
    def POST(request):
        if request.method == 'POST':
            form = RoleForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('role')


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
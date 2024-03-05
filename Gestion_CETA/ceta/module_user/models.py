from django.db import models
from rest_framework import serializers

class User(models.Model):
    #id_user = models.IntegerField(primary_key=True)
    fk_id_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name_user = models.CharField(max_length=255)
    password_user = models.CharField(max_length=255)

    def __str__(self):
        return self.name_user

class Role(models.Model):
    #id_role = models.IntegerField(primary_key=True)
    name_role = models.CharField(max_length=255)
    description_role = models.TextField()    

    def __str__(self):
        return self.name_role

#Enviar todos los datos del usuario luego de hacer el login
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Incluye todos los campos del modelo usuario en la serialización

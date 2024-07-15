# module_generic/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from django.db.models import Model
class GeneralView(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet
    ):
    model:Model = None
    serializer_class = None
    lookup_field = 'pk'
    def get_queryset(self):
        value = self.queryset
        if self.queryset is None:
            value = self.model.objects.filter(is_active=True)
        return value

class AllowedGeneralView(GeneralView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

class LogicDelete(DestroyModelMixin):
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

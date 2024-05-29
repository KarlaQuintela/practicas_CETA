from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets

class GeneralView(
        ListModelMixin,
        RetrieveModelMixin, 
        CreateModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet
    ):

    model = None
    serializer_class = None
    lookup_field = 'pk'
    def get_queryset(self):
        return self.model.objects.all()

class AllowedGeneralView(GeneralView):
    permission_classes = (IsAuthenticated,)
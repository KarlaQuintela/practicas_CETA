from rest_framework import viewsets
from django.db.models import Q
from rest_framework.response import Response
from .serializers import *
from ceta.module_contract.models import Contract

class ReportsViewset(viewsets.GenericViewSet):
     def clients_contracts(self, request, id):
        contracts = Contract.objects.select_related('Client').filter(fk_id_client=id)
        serializer = ContractSerializer(contracts, many=True)
        return Response(serializer.data)
       
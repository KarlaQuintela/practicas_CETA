from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.viewsets import GenericViewSet

from reportlab.pdfgen import canvas
from django.http import JsonResponse
import json

from .serializers import *
from ceta.module_contract.models import Contract, PaymentEmployee
from ceta.module_accounting.models import Bill

class ReportsViewset(GenericViewSet):    
    
     def clients_contracts(self, request, id_client):
        """Reporte de Contratos por Cliente: Este reporte proporciona una lista de todos los 
        contratos asociados a un cliente específico."""       
        contracts = Contract.objects.select_related('Client').filter(fk_id_client=id_client)
        serializer = Report_Clients_ContractSerializer(contracts, many=True)
        return Response(serializer.data)

     def month_bills(self, request, month):
        """Reporte de Facturación Mensual: Incluye detalles de todas las facturas generadas 
        en un mes específico, con información del cliente, el contrato asociado, 
        los trabajadores involucrados y los entregables."""       
        bills = Bill.objects.filter(month_bill=month)
        serializer = ReportBillSerializer(bills, many=True)
        return Response(serializer.data)
     
     def pending_payments(self, request):
        """Reporte de Pagos Pendientes: Este reporte muestra los pagos pendientes 
        de los clientes, incluyendo detalles de la factura, el plazo asociado y el contrato."""
        bills = Bill.objects.filter(is_paid=False)
        serializer = ReportPendingSerializer(bills, many=True)
        return Response(serializer.data)

     def pending_delivery(self, request):
        """Reporte de Entregables Pendientes: Este reporte muestra los entregables pendientes 
        incluyendo detalles del plazo asociado, el contrato y el trabajador."""
        delivers = PaymentEmployee.objects.filter(is_delivered=False)
        serializer = ReportPendingDeliverySerializer(delivers, many=True)
        return Response(serializer.data)

   
def generate_pdf(request):
   response = HttpResponse(content_type="application/pdf")
   response["Content-Disposition"] = 'attachment; filename="generated_report.pdf"'
   data = json.loads(request.body)
   p = canvas.Canvas(response)
   p.drawString(100, 800, "")
   y_position = 780
   for key, value in data.items():
      p.drawString(100, y_position, f"{key}: {value}")
      y_position -= 20
   p.showPage()
   p.save()
   return response


    



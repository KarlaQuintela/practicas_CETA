from django.shortcuts import render
from django.db.models import Q

from reportlab.pdfgen import canvas
from django.http import HttpResponse

def pdfExport(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="hello.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Courier", 28)
    p.drawString(60, 750, "Hola mundo")
    p.showPage()
    p.save()
    
    return response




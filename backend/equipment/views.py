import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dataset
from reportlab.pdfgen import canvas
from django.http import HttpResponse


# ---------------- CSV Upload & Analysis ----------------
@api_view(['POST'])
def upload_csv(request):
    file = request.FILES.get('file')

    if not file:
        return Response({"error": "No file uploaded"}, status=400)

    df = pd.read_csv(file)

    summary = {
        "total_equipment": len(df),
        "avg_flowrate": round(df["Flowrate"].mean(), 2),
        "avg_pressure": round(df["Pressure"].mean(), 2),
        "avg_temperature": round(df["Temperature"].mean(), 2),
        "type_distribution": df["Type"].value_counts().to_dict()
    }

    # Save to database
    Dataset.objects.create(
        total_equipment=summary["total_equipment"],
        avg_flowrate=summary["avg_flowrate"],
        avg_pressure=summary["avg_pressure"],
        avg_temperature=summary["avg_temperature"]
    )

    # Keep only last 5 records
    if Dataset.objects.count() > 5:
        Dataset.objects.first().delete()

    return Response(summary)


# ---------------- Dataset History ----------------
@api_view(['GET'])
def history(request):
    data = Dataset.objects.values().order_by('-uploaded_at')[:5]
    return Response(data)


# ---------------- PDF Report Generation ----------------
@api_view(['GET'])
def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 800, "Chemical Equipment Report")
    p.drawString(100, 770, "Generated from Dashboard")
    p.drawString(100, 740, "This report summarizes uploaded equipment data.")
    p.save()

    return response

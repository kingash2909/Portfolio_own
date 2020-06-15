from django.db import models

# Create your models here.
class certificate_Details(models.Model):
    cert_image = models.ImageField(upload_to="image/")
    cert_pdf = models.FileField(upload_to="pdf")
    cert_summary = models.CharField(max_length=200)
    cert_detailed = models.TextField(max_length=500)
    cert_frontend = models.CharField(max_length=200)
    cert_backend = models.CharField(max_length=200)



from django.db import models

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(upload_to="image/")
    pdf = models.FileField(upload_to="pdf")
    summary = models.CharField(max_length=200)
    cert_img = models.ImageField(upload_to="image/")
    cert_summary = models.CharField(max_length=200)







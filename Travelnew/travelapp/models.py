from django.db import models

# Create your models here.
class Destination(models.Model):
    destinationName=models.CharField(max_length=50)
    destinationDescription=models.TextField(max_length=300)
    destinationPrice=models.IntegerField()
    destinationImage=models.ImageField(upload_to='sample')

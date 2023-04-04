from django.db import models

# Create your models here.
class Register(models.Model):
    m_username=models.CharField(max_length=50)
    m_password=models.CharField(max_length=50)
    m_email=models.EmailField()
    m_phone=models.IntegerField()

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField(max_length=300)
    subject=models.CharField(max_length=200)
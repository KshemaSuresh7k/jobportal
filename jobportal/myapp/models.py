from django.db import models

# Create your models here.
class jobseeker(models.Model):
    name=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=30,null=True)
    age=models.IntegerField(max_length=50,null=True)
    qualification=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phonenumber=models.IntegerField(null=True)
    applyfor=models.CharField(max_length=50,null=True)
    workingmode=models.CharField(max_length=50,null=True)
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=20,null=True)

class employee(models.Model):
    name=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=30,null=True)
    age=models.IntegerField(max_length=50,null=True)
    email=models.CharField(max_length=50,null=True)
    phonenumber=models.IntegerField(null=True)
    username=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=20,null=True)
   

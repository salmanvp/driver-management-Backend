from django.db import models

class Vehcles(models.Model):
    Vehclebrand=models.CharField(max_length=20)
    vehclenumberplate=models.CharField(max_length=20)

class Driver(models.Model):
    Firstname=models.CharField(max_length=200,unique=True)
    Lastname=models.CharField(max_length=200,unique=True)
    Vehcle=models.ForeignKey(Vehcles,on_delete=models.CASCADE,null=True)

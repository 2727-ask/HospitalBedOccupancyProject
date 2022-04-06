from django.db import models

# Create your models here.

class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    contact = models.TextField(null =True)
    email = models.EmailField(null= True)
    url =models.CharField(max_length=500, null=True)
    address = models.TextField()


    def __str__(self):
        return self.name

class HospitalFacilities(models.Model):
    fk = models.ForeignKey(to=Hospital,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    desc = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.name
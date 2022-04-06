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


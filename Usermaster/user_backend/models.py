from django.db import models

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=255,null=True)
    email = models.CharField(max_length=255,null=True)
    role = models.CharField(max_length=255,null=True)
    isactive = models.BooleanField(default=True)


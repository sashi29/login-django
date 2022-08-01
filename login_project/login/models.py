from django.db import models

# Create your models here.
class create_user(models.Model): 
    name=models.CharField(max_length=50) 
    email=models.EmailField(max_length=50) 
    password1=models.CharField(max_length=40) 
    password2=models.CharField(max_length=40)
    def __str__(self):
        return self.name


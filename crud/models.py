from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Record(models.Model):
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.first_name + '   ' + self.last_name
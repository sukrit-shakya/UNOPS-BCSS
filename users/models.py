from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
    roletype = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.roletype)
    
class User(AbstractUser):
    role = models.ForeignKey(Role)


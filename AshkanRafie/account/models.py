from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    phone = models.EmailField(unique=True,null=True)
    bank_card_number = models.CharField(max_length=16,null=True,blank=True)
    # image = models.ImageField(upload_to='profile/', null=True,blank=True)
    national_id = models.CharField(max_length=10,unique=True,null=True,blank=True)

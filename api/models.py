from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


GENDER=(
    ('MALE','male'),
    ('FEMALE','female'),
    ('TRANSGENDER','transgender')
    
    
    )
class MyUser(AbstractUser):
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=100,choices=GENDER,null=True,blank=True)
    
    class Meta:
        verbose_name_plural='MyUser'
     

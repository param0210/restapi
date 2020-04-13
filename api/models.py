from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField


GENDER=(
    ('MALE','male'),
    ('FEMALE','female'),
    ('TRANSGENDER','transgender')
    
    
    )
class MyUser(AbstractUser):
    first_name=models.CharField(max_length=100,null=False,blank=False)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=100,choices=GENDER,null=True,blank=True)
    mobile_number=models.CharField(max_length=100,null=True,blank=True)
    
    class Meta:
        verbose_name_plural='Users'
           
RATING=(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    ) 
class ImageUpload(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True,blank=True,related_name='images')
    image=models.FileField(upload_to='photos/',null=True,blank=True)
    designation=models.CharField(max_length=100,blank=True,null=True)
    salary=models.IntegerField(blank=True,null=True)
    rating=models.PositiveIntegerField(choices=RATING,blank=True,null=True)
    created_on=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.models import Token
import os
from datetime import datetime
from django.utils import timezone


class HelloView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello all'}
        return Response(content)

class SignupViewSet(viewsets.ModelViewSet):
    permission_classes=(AllowAny,)
    serializer_class = MyUserSerializer

    
    def get_queryset(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
        return MyUser.objects.all()
    
    def create(self,request,*args,**kwargs):
        print("current time",datetime.now())
        print("timezone is",timezone.now())

        
        data=request.data
        if MyUser.objects.filter(username=data.get('username')).exists():
            return Response ({"message":"user already exists with same username"})
        if MyUser.objects.filter(mobile_number=data.get('mobile_number')).exists():
           return Response ({"message":"user already exists with same mobile_number"})
    
        user_dict={"first_name":data.get('first_name'),
                   "last_name":data.get('last_name'),
                   "password":data.get('password'),
                   "date_of_birth":data.get('date_of_birth'),
                   "gender":data.get('gender'),
                   "username":data.get('username'),
                   "email":data.get('username'),
                   "mobile_number":data.get('mobile_number'),
                   
            }
        
        
        try:
           user=MyUser.objects.create(**user_dict)
           user.set_password(data.get('password'))
           user.save()
           if user:
               token=Token.objects.get(user_id=user.id)
               user_dict.update({'token':token.key,'id':user.id})
            
           return Response({"data":user_dict,"message":"user registered successfully","status":status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"message":"user is not registered","status":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)

            
    @action(methods=['put'],detail=True,url_path='update')
    def update_profile(self,request,pk=None):
        print(pk)
        user=self.get_object()
        print(user.get_full_name())
        print(user.images)

        
        try:
            print(user.first_name or user.first_name==None)
            if user.first_name or user.first_name==None:
                user.first_name=request.data.get("first_name")
                user.save()
                
            return Response({"data":MyUserSerializer(user,allow_null=True,context={'request':request}).data,"message":"user updated successfully","status":status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)   
        
        except Exception as e:
            print(e)
            return Response({"message":"user is not updated","status":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)

       
    @action(methods=['delete'],detail=True,url_path='delete')
    def delete_profile(self,request,pk):
        user=self.get_object()
        user.delete()      
        return Response({"data":MyUserSerializer(user,allow_null=True,context={'request':request}).data,"message":"user deleted successfully","status":status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)   

class ImageUploadViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    serializer_class=(ImageUploadSerializer)
    
    def get_queryset(self):
        return ImageUpload.objects.all()
    
    def create(self,request,*args,**kwargs):
        try:
            
            image=ImageUpload.objects.create(user=request.user,image=request.data.get('image'))
            image.save()
            return Response({"message":"profile pic uploaded","status":status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"message":"profile pic is not uploaded","status":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)


class UserInfoViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    serializer_class=(MyUserSerializer)
    
    def get_queryset(self):

        user=MyUser.objects.all()

        return user.filter(images__salary='10000')









                
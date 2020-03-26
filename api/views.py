from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework import status
from .serializers import *
from rest_framework.authtoken.models import Token


class HelloView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello all'}
        return Response(content)

class SignupViewSet(viewsets.ModelViewSet):
    permission_classes=(AllowAny,)
    serializer_class = MyUserSerializer

    
    def get_queryset(self):
        return MyUser.objects.all()
    
    def create(self,request,*args,**kwargs):
        
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
               token=Token.objects.create(user_id=user.id)
               token.save()
               user_dict.update({'token':token.key,'id':user.id})
            
           return Response({"data":user_dict,"message":"user registered successfully","status":status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"message":"user is not registered","status":status.HTTP_400_BAD_REQUEST},status=status.HTTP_400_BAD_REQUEST)

               
                
from rest_framework import serializers
from .models import *



    
        
class ImageUploadSerializer(serializers.ModelSerializer):
    #image=serializers.SerializerMethodField()
    class Meta:
        model=ImageUpload
        fields='__all__'     
      
#     def get_image(self,obj):
#         return self.context['request'].build_absolute_uri(obj.image.url)
#       
#     def get_image_url(self, obj):
#         request = self.context.get("request")
#         return request.build_absolute_uri(obj.image.url)


class MyUserSerializer(serializers.ModelSerializer):
    images=ImageUploadSerializer(read_only=True,many=True)
#     images=serializers.FileField(source='imageupload.image')
#     designation=serializers.CharField(source='imageupload.designation')
    firstname=serializers.CharField(source='first_name')
    full_name=serializers.CharField(source='get_full_name')

    class Meta:
        model=MyUser
        fields=('email','first_name','last_name','firstname','full_name','images')    
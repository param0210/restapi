from django.contrib import admin
from django.contrib.auth.models import Group
from.models import *


def rating(modeladmin,request,queryset):
    queryset.update(rating=1)
    
    rating.short_description="change rating"
         
class MyUsreA(admin.ModelAdmin):
    exclude=('groups','user_permissions')
    list_display=('username','email','first_name','last_name')
    list_filter=('gender',)
    search_fields=('email',)
  
class ImageUploadA(admin.ModelAdmin):
    list_display=('user','image','salary','designation','rating')
    list_filter=('designation',)
    search_fields=('user__username',)  
    actions=[rating]
    
    
admin.site.register(MyUser,MyUsreA)
admin.site.register(ImageUpload,ImageUploadA)
admin.site.unregister(Group)

'''
change the admin header
'''
admin.site.site_header=" Django RestFramework"
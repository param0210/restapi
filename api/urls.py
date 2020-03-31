from django.conf.urls import url,include
from .views import SignupViewSet
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'signup', views.SignupViewSet,basename='signup')
router.register(r'upload', views.ImageUploadViewSet,basename='upload')
router.register(r'user', views.UserInfoViewSet,basename='user')

urlpatterns=[
    url(r'^/',include(router.urls)),
    url('hello/',views.HelloView.as_view(),name='hello')
    ]



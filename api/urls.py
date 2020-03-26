from django.conf.urls import url,include
from .views import SignupViewSet
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'signup', views.SignupViewSet,basename='signup')

urlpatterns=[
    url(r'^/',include(router.urls)),
    url('hello/',views.HelloView.as_view(),name='hello')
    ]



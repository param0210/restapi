from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyUser
from rest_framework.authtoken.models import Token   


@receiver(post_save, sender=MyUser)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user_id=instance.id)


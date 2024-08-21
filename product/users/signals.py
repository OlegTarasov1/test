from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Balance


@receiver(post_save, sender=get_user_model())
def create_balance(sender, instance, created, **kwargs):
    if created:
        Balance.objects.create(user=instance, balance = 1000.00)
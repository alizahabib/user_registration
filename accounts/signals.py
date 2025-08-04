# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, Group

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        default_group, _ = Group.objects.get_or_create(name="Student")
        profile.groups.add(default_group)

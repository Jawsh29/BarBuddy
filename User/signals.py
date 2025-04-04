from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver


# Profile Creation


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if not instance.is_superuser:
            Profile.objects.create(staff=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
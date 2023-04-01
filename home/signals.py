from django.db.models.signals import pre_save
from .models import AboutMe
from django.dispatch import receiver


@receiver([pre_save], sender=AboutMe)
def delete_all_objects(sender, instance, **kwargs):
    AboutMe.objects.all().delete()

from django.db.models.signals import pre_delete, pre_save
from django.dispatch.dispatcher import receiver
from .models import *

@receiver(pre_save, sender=Audio)
def delete_file(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_file = Audio.objects.get(pk=instance.pk).photo
        except Audio.DoesNotExist:
            return False
        new_file = instance.photo
        if not old_file == new_file:
            old_file.delete(save=False)

@receiver(pre_delete, sender=Audio)
def delete_file(sender, instance, **kwargs):
    instance.photo.delete(False)

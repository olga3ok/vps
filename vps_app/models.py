import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class VPS(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('blocked', 'Blocked'),
        ('stopped', 'Stopped'),
    ]

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    cpu = models.IntegerField()
    ram = models.IntegerField()
    hdd = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.uid)
    
@receiver(pre_save, sender=VPS)
def generate_uid(sender, instance, **kwargs):
    if not instance.uid:
        instance.uid = uuid.uuid4()
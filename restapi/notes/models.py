import uuid

from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver


class Dataset(models.Model):
    id = models.CharField(max_length=64, primary_key=True,
                          default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)


"""
class Action(models.Model):
    id = models.CharField(max_length=64, primary_key=True,
                          default=uuid.uuid4, editable=False)
    rank = models.PositiveIntegerField()
    maxRank = models.PositiveIntegerField()
    percentage = models.DecimalField(max_digits=12, decimal_places=8)
    imagepath = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)
    objectlabel = models.CharField(
        max_length=256, null=True, blank=True, editable=True)
    obj = models.ForeignKey(
        Object,
        on_delete=models.SET_NULL,
        related_name="actions",
        null=True,
    )

@receiver(pre_delete, sender=Object)
def handlePreDelete(sender, **kwargs):
    pass
    instance = kwargs['instance']
    actions = instance.actions.all()
    if(len(actions) > 0):
        for action in actions:
            action.objectlabel = instance.label
            action.save()

@receiver(pre_delete, sender=Object)
def handlePostDelete(sender, **kwargs):
    pass
    instance = kwargs['instance']
    actions = instance.actions.all()
    if(len(actions) > 0):
        for action in actions:
            action.objectlabel = instance.label
            action.save()
            
pre_delete.connect(handlePreDelete, sender=Object)
post_delete.connect(handlePostDelete, sender=Object)
"""

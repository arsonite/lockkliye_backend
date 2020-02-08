import uuid

from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver


class Label(models.Model):
    id = models.CharField(max_length=64, primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    color = models.CharField(max_length=6, unique=True, editable=True)
    title = models.CharField(max_length=256, unique=True, editable=True)
    description = models.CharField(max_length=512, unique=True, editable=True)


class Note(models.Model):
    id = models.CharField(max_length=64, primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256, editable=True)
    content = models.TextField(editable=True)
    labels = models.ManyToManyField(
        Label,
        related_name='noteLabels',
    )


class List(models.Model):
    id = models.CharField(max_length=64, primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256, editable=True)
    labels = models.ManyToManyField(
        Label,
        related_name='listLabels'
    )


class Folder(models.Model):
    id = models.CharField(max_length=64, primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256, null=True,
                             blank=True, editable=True)
    subfolders = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        related_name='folders',
        null=True,
    )
    notes = models.ForeignKey(
        Note,
        on_delete=models.SET_NULL,
        related_name='notes',
        null=True,
    )
    lists = models.ForeignKey(
        List,
        on_delete=models.SET_NULL,
        related_name='lists',
        null=True,
    )

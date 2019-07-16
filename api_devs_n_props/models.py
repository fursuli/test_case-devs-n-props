from django.db import models

# Create your models here.

class Device(models.Model):
    d_name = models.CharField(max_length=68, null=False, blank=True)
    properties = models.ManyToManyField(to='Property', related_name='properties')

class Property(models.Model):
    types = [
        ('json', 'json'),
        ('plaintext', 'plaintext'),
        ('binary', 'binary')
    ]

    p_name = models.CharField(max_length=68, null=False, blank=False)
    content = models.TextField(max_length=200, null=True, blank=True)
    type = models.CharField(choices=types, max_length=9, default='plaintext')
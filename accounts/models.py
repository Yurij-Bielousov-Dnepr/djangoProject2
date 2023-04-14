# models.py
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from art_event.models import Favorites
from helpy.models import Region, Language

class Visitor(models.Model):
    userNick = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=[('Helper', 'Helper'), ('Customer', 'Customer')], default='Customer')
    district = models.ManyToManyField(Region)
    languages = models.ManyToManyField(Language)
    is_sponsor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.userNick

# models.py
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from art_event.models import Favorites
from helpy.models import Region, Language
from django.utils import timezone


class Visitor(models.Model):
    user = models.OneToOneField( User, on_delete=models.CASCADE, related_name='visitor' )
    userNick = models.CharField(max_length=255)
    password = models.CharField( max_length=255, blank=False )
    category = models.CharField(max_length=255, choices=[('Helper', 'Helper'), ('Customer', 'Customer')], default='Customer')
    district = models.ManyToManyField(Region)
    languages = models.ManyToManyField(Language)
    is_sponsor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    last_activity = models.DateTimeField( auto_now=True )
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE, null=True, blank=True)
    about_me = models.TextField( blank=True )  # новое поле "обо мне"

    def __str__(self):
        return self.userNick

class Stats(models.Model):
    date = models.DateField(auto_now_add=True)
    active_helpers = models.IntegerField(default=0)
    help_requests = models.IntegerField(default=0)
    online_users = models.IntegerField(default=0)
    last_activity = models.ForeignKey(Visitor, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Stats"

    def __str__(self):
        return f"{self.date} - Active helpers: {self.active_helpers}, Help requests: {self.help_requests}, Online users: {self.online_users}"

# models.py
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from art_event.models import Favorites, Event, Article
from django.contrib.auth.models import AbstractBaseUser
from helpy.models import Region, Language
from django.utils import timezone


class Visitor(AbstractBaseUser):
    user_login = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="visitor"
    )
    userNick = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=False)
    category = models.CharField(
        max_length=255,
        choices=[("Helper", "Helper"), ("Customer", "Customer")],
        default="Customer",
    )
    district = models.ManyToManyField(Region)
    languages = models.ManyToManyField(Language)
    is_sponsor = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    last_activity = models.DateTimeField(auto_now=True)
    favorites = models.ForeignKey(
        Favorites, on_delete=models.CASCADE, null=True, blank=True
    )
    about_me = models.TextField(blank=True)

    @property
    def is_authenticated(self):
        return True if self.id else False

    def __str__(self):
        return self.userNick


class Stats(models.Model):
    date = models.DateField(auto_now_add=True)
    active_helpers = models.IntegerField(default=0)
    help_requests = models.IntegerField(default=0)
    online_users = models.IntegerField(default=0)
    last_activity = models.ForeignKey(
        Visitor, on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        verbose_name_plural = "Stats"

    def __str__(self):
        return f"{self.date} - Active helpers: {self.active_helpers}, Help requests: {self.help_requests}, Online users: {self.online_users}"


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name


class Region(models.Model):
    CHAWENG = "Chaweng"
    LAMAI = "Lamai"
    LIPA_NOI = "Lipa Noi"
    NATHON = "Nathon"
    BANG_BOR = "Bang Bor"
    MAENAM = "Maenam"
    BOPHUT = "Bophut"
    CHOENG_MON = "Choeng Mon"
    HUA_THANON = "Hua Thanon"

    REGION_CHOICES = [
        ("", "Choose all"),  # добавляем пустой элемент
        (CHAWENG, "Chaweng"),
        (LAMAI, "Lamai"),
        (LIPA_NOI, "Lipa Noi"),
        (NATHON, "Nathon"),
        (BANG_BOR, "Bang Bor"),
        (MAENAM, "Maenam"),
        (BOPHUT, "Bophut"),
        (CHOENG_MON, "Choeng Mon"),
        (HUA_THANON, "Hua Thanon"),
    ]

    name = models.CharField(max_length=255, choices=REGION_CHOICES)

    def __str__(self):
        return self.name


class Language(models.Model):
    UKRAINIAN = "uk"
    THAI = "th"
    ENGLISH = "en"
    FRENCH = "fr"
    ITALIAN = "it"
    GERMAN = "de"
    RUSSIAN = "ru"

    LANGUAGE_CHOICES = [
        (UKRAINIAN, "Українська"),
        (THAI, "ไทย"),
        (ENGLISH, "English"),
        (FRENCH, "Français"),
        (ITALIAN, "Italiano"),
        (GERMAN, "Deutsch"),
        (RUSSIAN, "Русский"),
    ]

    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return self.language


class SupportLevel(models.Model):
    LEVEL_CHOICES = [
        (1, "Level 1"),
        (2, "Level 2"),
        (3, "Level 3"),
    ]
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __str__(self):
        return f"Level {self.level}"


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, null=True, blank=True
    )
    is_favorite = models.BooleanField(default=False)


class Level(models.Model):
    LEVEL_CHOICES = [
        (1, "Level 1"),
        (2, "Level 2"),
        (3, "Level 3"),
    ]
    level = models.IntegerField(choices=LEVEL_CHOICES)

    def __str__(self):
        return f"Level {self.level}"

from django.db import models
from django.contrib.auth.models import User

from comic.models import ComicBook


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    read = models.ManyToManyField(ComicBook, blank=True, related_name="profiles_through_read")
    wishlist = models.ManyToManyField(ComicBook, blank=True, related_name="profiles_through_wishlist")

    def __str__(self):
        return self.user.username

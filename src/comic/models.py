from django.db import models

from publisher.models import Publisher


class ComicBook(models.Model):
    title = models.CharField(max_length=255)
    cover = models.ImageField()
    publisher = models.ForeignKey(Publisher, related_name="comic_books", on_delete=models.CASCADE)
    release_date = models.DateField()

    def __str__(self):
        return self.title

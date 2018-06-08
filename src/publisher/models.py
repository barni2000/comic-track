from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    foundation_year = models.IntegerField()

    def __str__(self):
        return self.name

from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BigIntegerField()
    description = models.TextField()
    book = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BigIntegerField()
    description = models.TextField()
    book = models.CharField(max_length=100)
    picture = models.FileField(upload_to='characters/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

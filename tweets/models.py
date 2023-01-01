from django.db import models


class Tweet(models.Model):
    content = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)


    def __str__(self):
        return f'tweet: {self.id}'
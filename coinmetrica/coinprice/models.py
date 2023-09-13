from django.db import models

class coins(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField()

    def __str__(self):
        return self.title


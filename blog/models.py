from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    # TextField permite armazenar HTML
    content = models.TextField()
    # Data de publicação automática na criação, mas editável se necessário
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
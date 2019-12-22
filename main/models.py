from django.db import models
from django.utils import timezone


# Create your models here.
class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_publish = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.tutorial_title


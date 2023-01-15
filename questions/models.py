from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return f"{self.id}- {self.title}"

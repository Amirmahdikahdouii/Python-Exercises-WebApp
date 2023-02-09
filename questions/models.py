from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.id}- {self.title}"


class QuestionAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="User")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Question")
    file = models.FileField(upload_to='questions/answers/')

    def __str__(self):
        return f"{self.id}- {self.user.username}"

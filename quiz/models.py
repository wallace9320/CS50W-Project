from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    def serialize(self):
        return {
            "id": self.id,
        }
    

class Quiz(models.Model):
    owner = models.ForeignKey("User", on_delete=models.CASCADE, related_name="owner")
    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    answered = models.ManyToManyField("User", blank=True, related_name="answered")

    def serialize(self):
        return {
            "id": self.id,
            "owner": self.owner.username,
            "title": self.title,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "answered": [user.username for user in self.answered.all()]
        }


class Question(models.Model):
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, related_name="quiz")
    question_description = models.CharField(max_length=300)


class Option(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE, related_name="question")
    option_description = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    chosen_user = models.ManyToManyField("User", blank=True, related_name="chosen_user")


class Score(models.Model):
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, related_name="quiz_score")
    answerer = models.ForeignKey("User", on_delete=models.CASCADE, related_name="answerer")
    result = models.IntegerField()
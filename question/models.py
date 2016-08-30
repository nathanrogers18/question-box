from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    score = models.IntegerField(default=0)

    def __str__(self):
        return "{} has {} points".format(self.user, self.score)


class Tag(models.Model):
    topic = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.topic)


class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.TextField()
    tag = models.ManyToManyField(Tag)
    vote = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.user, self.title, self.text, self.tag, self.timestamp)


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    text = models.TextField()
    vote = models.IntegerField(default=0)
    accepted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.user, self.question, self.text, self.timestamp)


class Comment(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    question = models.ForeignKey(Question, blank=True, null=True)
    answer = models.ForeignKey(Answer, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.user, self.text, self.question, self.answer, self.timestamp)

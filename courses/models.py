from django.conf import settings
from django.db import models
from django.utils import timezone


class Course(models.Model):
    title = models.CharField(max_length=2000)
    description = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=2000)
    content = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text[:150]

 
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class TestAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    started_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)

    score = models.IntegerField(default=0)
    passed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"


class UserAnswer(models.Model):
    attempt = models.ForeignKey(TestAttempt, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.is_correct = self.selected_answer.is_correct
        super().save(*args, **kwargs)
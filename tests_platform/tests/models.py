from django.db import models

from django.contrib.auth.models import User

# Model Kursu
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE)  # Nauczyciel prowadzący

    def __str__(self):
        return self.title

# Model Testu
class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, related_name='tests', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = [
        ('single', 'Single Choice'),
        ('multiple', 'Multiple Choice'),
        ('open', 'Open Question'),
    ]
    
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES)

    def __str__(self):
        return f"{self.text} ({self.get_question_type_display()})"

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} - {'Correct' if self.is_correct else 'Incorrect'}"

class Result(models.Model):
    student = models.ForeignKey(User, related_name='results', on_delete=models.CASCADE)  # Uczeń
    test = models.ForeignKey(Test, related_name='results', on_delete=models.CASCADE)
    score = models.FloatField()
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.test.title} - {self.score}"

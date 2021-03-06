from django.db import models
from django.contrib.auth.models import User
from quiz.models import Quiz
# Create your models here.

AVATAR_CHOICES = {
    ('boy_avatar1', 'Boy Avatar1'),
    ('boy_avatar2', 'Boy Avatar2'),
    ('boy_avatar3', 'Boy Avatar3'),
    ('boy_avatar4', 'Boy Avatar4'),
    ('girl_avatar1', 'Girl Avatar1'),
    ('girl_avatar2', 'Girl Avatar2'),
    ('girl_avatar3', 'Girl Avatar3'),
    ('girl_avatar4', 'Girl Avatar4'),
}

GRADE_CHOICES = {
    ('Pre-K', 'Pre-K'),
    ('Kindergarten', 'Kindergarten'),
    ('1st Grade', '1st Grade'),
    ('2nd Grade', '2nd Grade'),
    ('3rd Grade', '3rd Grade'),
}

class Student(models.Model):
    instuctor = models.ForeignKey(User, related_name='students', on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=50, choices=AVATAR_CHOICES)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES)
    level = models.IntegerField(default=1)
    reward = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, related_name='quizzes', on_delete = models.CASCADE )
    quiz = models.ForeignKey(Quiz, related_name='taken_quizzes', on_delete = models.CASCADE )
    score = models.IntegerField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
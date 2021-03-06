from django.db import models
from user.models import User

# Create your models here.

SUBJECT_CHOICES = {
    ('Math', 'Math'),
    ('English', 'English'),
    ('Spanish', 'Spanish'),
    ('Korean', 'Korean'), 
    ('Science', 'Science'),
    ('Social Studies', 'Social Studies')
}

DIFFICULTY_CHOICES = {
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('difficult', 'difficult')
}

GRADE_CHOICES = {
    ('Pre-K', 'Pre-K'),
    ('Kindergarten', 'Kindergarten'),
    ('1st Grade', '1st Grade'),
    ('2nd Grade', '2nd Grade'),
    ('3rd Grade', '3rd Grade'),
}

class Quiz(models.Model):
    title = models.CharField(max_length=250)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES, blank = True)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, blank = True)
    grade = models.CharField(max_length=50, choices=GRADE_CHOICES, blank = True)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='quizzes', on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    text = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.text 

class Answer(models.Model):
    text = models.CharField(max_length=250)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text 
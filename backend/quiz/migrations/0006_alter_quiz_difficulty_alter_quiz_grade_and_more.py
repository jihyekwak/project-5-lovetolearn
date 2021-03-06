# Generated by Django 4.0.4 on 2022-04-21 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_quiz_grade_alter_quiz_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.CharField(blank=True, choices=[('medium', 'medium'), ('easy', 'easy'), ('difficult', 'difficult')], max_length=20),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='grade',
            field=models.CharField(blank=True, choices=[('2nd Grade', '2nd Grade'), ('Pre-K', 'Pre-K'), ('3rd Grade', '3rd Grade'), ('Kindergarten', 'Kindergarten'), ('1st Grade', '1st Grade')], max_length=50),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='subject',
            field=models.CharField(blank=True, choices=[('Math', 'Math'), ('English', 'English'), ('Social Studies', 'Social Studies'), ('Spanish', 'Spanish'), ('Korean', 'Korean'), ('Science', 'Science')], max_length=20),
        ),
    ]

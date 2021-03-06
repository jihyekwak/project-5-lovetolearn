# Generated by Django 4.0.4 on 2022-04-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_quiz_difficulty_alter_quiz_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulty',
            field=models.CharField(blank=True, choices=[('difficult', 'difficult'), ('easy', 'easy'), ('medium', 'medium')], max_length=20),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='grade',
            field=models.CharField(blank=True, choices=[('Kindergarten', 'Kindergarten'), ('Pre-K', 'Pre-K'), ('1st Grade', '1st Grade'), ('2nd Grade', '2nd Grade'), ('3rd Grade', '3rd Grade')], max_length=50),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='subject',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Social Studies', 'Social Studies'), ('Spanish', 'Spanish'), ('Math', 'Math'), ('Science', 'Science'), ('Korean', 'Korean')], max_length=20),
        ),
    ]

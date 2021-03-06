# Generated by Django 4.0.4 on 2022-04-20 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
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
            field=models.CharField(blank=True, choices=[('1st Grade', '1st Grade'), ('2nd Grade', '2nd Grade'), ('Kindergarten', 'Kindergarten'), ('3rd Grade', '3rd Grade'), ('Pre-k', 'Pre-K')], max_length=50),
        ),
    ]

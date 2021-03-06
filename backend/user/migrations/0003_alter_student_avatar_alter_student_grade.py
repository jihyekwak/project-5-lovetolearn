# Generated by Django 4.0.4 on 2022-05-02 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_student_grade_alter_takenquiz_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avatar',
            field=models.CharField(choices=[('girl_avatar1', 'Girl Avatar1'), ('boy_avatar2', 'Boy Avatar2'), ('girl_avatar2', 'Girl Avatar2'), ('girl_avatar3', 'Girl Avatar3'), ('girl_avatar4', 'Girl Avatar4'), ('boy_avatar4', 'Boy Avatar4'), ('boy_avatar3', 'Boy Avatar3'), ('boy_avatar1', 'Boy Avatar1')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('2nd Grade', '2nd Grade'), ('Pre-K', 'Pre-K'), ('3rd Grade', '3rd Grade'), ('1st Grade', '1st Grade'), ('Kindergarten', 'Kindergarten')], max_length=50),
        ),
    ]

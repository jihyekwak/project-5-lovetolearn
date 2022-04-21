# Generated by Django 4.0.4 on 2022-04-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_student_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('Pre-K', 'Pre-K'), ('1st Grade', '1st Grade'), ('Kindergarten', 'Kindergarten'), ('2nd Grade', '2nd Grade'), ('3rd Grade', '3rd Grade')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='reward',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0006_result_question_alter_result_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='question',
        ),
        migrations.AlterField(
            model_name='result',
            name='student_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
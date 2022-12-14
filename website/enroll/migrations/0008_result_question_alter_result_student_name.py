# Generated by Django 4.1.2 on 2022-10-21 08:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enroll', '0007_remove_result_question_alter_result_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='enroll.question'),
        ),
        migrations.AlterField(
            model_name='result',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

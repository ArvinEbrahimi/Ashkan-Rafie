# Generated by Django 5.1.6 on 2025-04-11 15:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Azmoon', '0003_remove_choice_question_remove_examattempt_exam_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='azmoon_test_results', to=settings.AUTH_USER_MODEL),
        ),
    ]

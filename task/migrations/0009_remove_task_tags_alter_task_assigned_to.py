# Generated by Django 5.1.6 on 2025-04-28 14:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_remove_task_is_completed_task_due_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(related_name='assigned_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
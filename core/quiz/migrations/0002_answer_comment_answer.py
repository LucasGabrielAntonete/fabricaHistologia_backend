# Generated by Django 4.2.13 on 2024-07-10 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='comment_answer',
            field=models.TextField(default=''),
        ),
    ]
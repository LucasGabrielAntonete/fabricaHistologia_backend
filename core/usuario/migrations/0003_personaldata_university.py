# Generated by Django 4.2.13 on 2024-07-10 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_personaldata'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='university',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
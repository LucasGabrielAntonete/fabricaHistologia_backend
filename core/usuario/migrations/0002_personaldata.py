# Generated by Django 4.2.13 on 2024-07-10 22:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registration', models.CharField(max_length=20)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=20)),
                ('education_level', models.CharField(choices=[('Médio', 'Médio'), ('Superior', 'Superior'), ('Pós-Graduação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Doutorado', 'Doutorado'), ('Pós-Doutorado', 'Pós-Doutorado')], default='Médio', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dados Pessoais',
                'verbose_name_plural': 'Dados Pessoais',
                'ordering': ['name'],
            },
        ),
    ]

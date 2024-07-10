# Generated by Django 4.2.13 on 2024-07-10 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploader', '0001_initial'),
        ('fabrica_histologia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slidemicroscopypost',
            name='autor_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='slidemicroscopypost',
            name='image_slide',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
        migrations.AddField(
            model_name='slidemicroscopypost',
            name='organ',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabrica_histologia.organ'),
        ),
        migrations.AddField(
            model_name='slidemicroscopypost',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabrica_histologia.specie'),
        ),
        migrations.AddField(
            model_name='point',
            name='slide',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabrica_histologia.slidemicroscopypost'),
        ),
        migrations.AddField(
            model_name='organ',
            name='image_organ',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='uploader.image'),
        ),
        migrations.AddField(
            model_name='organ',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fabrica_histologia.system'),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_livre_fichier_audio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livre',
            name='fichier_audio',
        ),
        migrations.AddField(
            model_name='livre',
            name='audio',
            field=models.URLField(blank=True, help_text='Lien du livre audio', max_length=500, null=True),
        ),
    ]

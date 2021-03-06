# Generated by Django 2.2 on 2022-05-10 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220504_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.CharField(blank=True, choices=[('Cognitive', 'Cognitive Skills'), ('Management', 'Management Skills'), ('Interpersonal', 'Interpersonal Skills'), ('Other skills', 'Other skills')], max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_experience',
            field=models.TextField(choices=[('Less than a year', 'Less than a year'), ('one to three year', '1 to 3'), ('three to five years', '3 to 5 years'), ('Five years and more', '  5+ years')], max_length=30),
        ),
    ]

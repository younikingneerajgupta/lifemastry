# Generated by Django 4.2.4 on 2023-08-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserRegistrationForm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(default='neerajgupta', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='mode',
            field=models.CharField(choices=[('home', 'Home'), ('away', 'Away')], default=8851659266, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default=885165, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student')], default='blank', max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subjects',
            field=models.CharField(blank=True, choices=[('hindi', 'Hindi'), ('english', 'English'), ('math', 'Math'), ('science', 'Science'), ('history', 'History')], max_length=10, null=True),
        ),
    ]

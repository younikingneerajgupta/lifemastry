from django.db import models

class UserProfile(models.Model):
    # Basic Information
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='profile_images/')

    # Contact Information
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Mode (Home/Away)
    MODE_CHOICES = [
        ('home', 'Home'),
        ('away', 'Away'),
    ]
    mode = models.CharField(max_length=4, choices=MODE_CHOICES)

    # Skills
    skills = models.TextField(blank=True, null=True)

    # Subjects
    SUBJECT_CHOICES = [
        ('hindi', 'Hindi'),
        ('english', 'English'),
        ('math', 'Math'),
        ('science', 'Science'),
        ('history', 'History'),
    ]
    subjects = models.CharField(max_length=10, choices=SUBJECT_CHOICES, blank=True, null=True)

    select_classes = [
        ('class i', 'Class I'),
        ('class ii', 'Class II'),
        ('class iii', 'Class III'),
        ('class iv', 'Class IV'),
        ('class v', 'Class V'),
        ('class vi', 'Class VI'),
        ('class vii', 'Class VII'),
        ('class viii', 'Class VIII'),
        ('class ix', 'Class IX'),
        ('class x', 'Class X'),
        ('class xi', 'Class XI'),
        ('class xii', 'Class XII'),
    ]    
    select_class = models.CharField(max_length=12, choices=select_classes, blank=True, null=True)
    # Password
    password = models.CharField(max_length=128)  # You should consider using Django's built-in password hashing

    # Role
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=7, choices=ROLE_CHOICES)
    sub = models.TextField()
    def __str__(self):
        return self.full_name

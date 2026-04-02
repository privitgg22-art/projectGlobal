from django.db import models
from unicodedata import category


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    github = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="experiences")
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} - {self.university}"


class Skill(models.Model):
    LEVEL_CHOICES = [
        ('beginner, Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('devops', 'Devops'),
        ('other', 'Other'),
    ]


profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
name = models.CharField(max_length=50)
level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')


class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="education")
    university = ""
    degree = ""
    field = ""
    start_year = ""
    end_year = ""
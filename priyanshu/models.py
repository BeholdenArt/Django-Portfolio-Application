from os import link
from django.db import models


# Home Section
class Home(models.Model):
    name = models.CharField(max_length=20)
    greetings_1 = models.CharField(max_length=5)
    greetings_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')

    # save time of modification
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# About Section (First Scroll Down)
class About(models.Model):
    heading = models.CharField(max_length=50)
    career = models.CharField(max_length=40)
    description = models.TextField(blank=False)
    profile_img = models.ImageField(upload_to='about/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career


# Profile Link (Social Link)
class Profile(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    social_name = models.CharField(max_length=40)
    link = models.URLField(max_length=250)

    def __str__(self):
        return self.social_name


# Skills Section
# Skill category
class Category(models.Model):
    name = models.CharField(max_length=40)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name


# Skills list
class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=40)

    def __str__(self):
        return self.skill_name


# Resume Upload
class Resume(models.Model):
    name = models.CharField(max_length=80)
    link = models.FileField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Portfolio Section
# Projects
class Portfolio(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title


# Contact Form
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name

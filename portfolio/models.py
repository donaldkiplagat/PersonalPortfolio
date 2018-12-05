from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db.models import Q

import datetime as dt

# Create your models here.
class skills(models.Model):
    skillslogo = models.ImageField(upload_to='skillslogo/')
    skills = models.CharField(max_length=100)

    def __str__(self):
        return self.skills

    def save_skills(self):
        self.save()

    @classmethod
    def delete_skills(cls,skills):
        cls.objects.filter(skills=skills).delete()

class technologies(models.Model):
    techlogo = models.ImageField(upload_to='techlogo/')
    technologies = models.CharField(max_length=100)

    def __str__(self):
        return self.technologies

    def save_technology(self):
        self.save()

    @classmethod
    def delete_technology(cls,technologies):
        cls.objects.filter(technologies=technologies).delete()

class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatar/')
    description = HTMLField()
    nationality =models.CharField(max_length=100)
    firstname =models.CharField(max_length=100)
    secondname =models.CharField(max_length=100)
    email = models.EmailField()
    phone_number =models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = HTMLField()
    role= models.CharField(max_length=255)
    githublink= models.CharField(max_length=255)
    weblink= models.CharField(max_length=255)
    logo = models.ImageField(upload_to='projectlogo/')
    screenshot = models.ImageField(upload_to='projectscreenshot/')
    technologies = models.ManyToManyField(technologies)


    def __str__(self):
        return self.title

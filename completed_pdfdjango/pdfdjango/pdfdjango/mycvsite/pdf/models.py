from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()
    summary = models.TextField(max_length=2000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    priviouswork = models.TextField(max_length=3000)
    skills = models.TextField(max_length=4000)
    certifications = models.TextField(max_length=4000)

    def __str__(self):
        return self.name




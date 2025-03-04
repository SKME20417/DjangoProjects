from django.db import models

# Create your models here.

class Link(models.Model):
    address = models.CharField(max_length=2000, blank=True, null=True)
    name = models.CharField(max_length=2000, blank=True, null=True)


    def __str__(self):
        if self.name==None:
            return "ERROR NAME IS NULL"
        return self.name


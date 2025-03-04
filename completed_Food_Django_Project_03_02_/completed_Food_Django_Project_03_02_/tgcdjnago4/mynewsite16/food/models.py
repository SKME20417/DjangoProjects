from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Items(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    quntity = models.IntegerField()
    image = models.CharField(max_length=5000, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT27gTKHqKhHk3i-EiarE5Q9IND_awvKaKjxw&s")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food:detail', kwargs={"pk" : self.pk})
        
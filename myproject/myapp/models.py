from django.db import models
from django.contrib.auth.models import User

class Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(null=True,blank=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

class Marks(models.Model):
    details = models.ForeignKey(Details, on_delete=models.CASCADE)
    maths = models.IntegerField()
    english = models.IntegerField()
    science = models.IntegerField()
    






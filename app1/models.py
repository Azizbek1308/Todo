from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=20, blank=True)
    age = models.IntegerField()
    def __str__(self):
        return self.name

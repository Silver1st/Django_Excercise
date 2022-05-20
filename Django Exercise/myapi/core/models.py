from django.db import models
from flask import request

# Create your models here.

class Student(models.Model):
    #name = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Quote(models.Model):
    text = models.TextField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.text[:50]

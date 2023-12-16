from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    description = models.CharField(max_length=100)
    salary = models.IntegerField()

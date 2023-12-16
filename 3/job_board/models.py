from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()

# CRUD operations
# create
# update
# read
# delete

# model manager -> objects
# JobPosting.objects.all()
# JobPosting.objects.get(id=1)
# JobPosting.objects.filter(company="abc tech")
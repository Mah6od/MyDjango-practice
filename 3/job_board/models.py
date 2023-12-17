from django.db import models

# Create your models here.
class JobPosting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company} | Active: {self.is_active}"

# CRUD operations
# create
# update
# read
# delete

# model manager -> objects
# JobPosting.objects.all()
# JobPosting.objects.get(id=1)
# JobPosting.objects.filter(company="abc tech")
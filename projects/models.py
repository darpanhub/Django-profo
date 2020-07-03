from django.db import models

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=150,blank=False)
    content = models.TextField(blank=False)
    developers = models.CharField(max_length=30,blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=True,null=True)
    project_link = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.title


from django.db import models

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=150,blank=False,help_text="please enter title of project")
    content = models.TextField(blank=False,help_text="please enter content of project")
    developers = models.CharField(max_length=30,blank=False,help_text="please enter developer name of project")
    start_date = models.DateField(blank=False,help_text="please enter start date project")
    end_date = models.DateField(blank=True,null=True)
    project_link = models.CharField(max_length=200,blank=True)
    project_img = models.ImageField(null=True,blank=False)
    def __str__(self):
        return self.title


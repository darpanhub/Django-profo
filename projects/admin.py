from django.contrib import admin
from projects.models import project

# Register your models here.
class projectAdmin (admin.ModelAdmin):
    list_display = ('title','developers','start_date',)
admin.site.register(project,projectAdmin)

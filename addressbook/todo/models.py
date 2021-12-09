from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    class Meta:
        app_label = 'todo'

    def _str_(self):
        return self.title
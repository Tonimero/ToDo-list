from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, blank=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
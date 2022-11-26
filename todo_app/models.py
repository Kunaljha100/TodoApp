from django.db import models

# Create your models here.


class Todo_Task(models.Model):
    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    task_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    


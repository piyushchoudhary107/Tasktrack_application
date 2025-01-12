from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Work', 'Work'),
    ('Personal', 'Personal'),
    ('Urgent', 'Urgent'),
    ('Other', 'Other'),
]

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title

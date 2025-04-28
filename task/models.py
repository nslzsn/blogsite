from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

STATUS_CHOICES = [
    ('pending', 'Bekliyor'),
    ("in_progress", 'Devam Ediyor'),
    ('done', 'Tamamlandı'),
]



class Task(models.Model):
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    #tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
   

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    task = models.ForeignKey("Task", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Yorum ({self.user.username}) - {self.task.title}"
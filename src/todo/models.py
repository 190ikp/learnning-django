from django.db import models

class Post(models.Model):
    title = models.CharField(
        max_length = 20
    )
    post = models.CharField(
        max_length = 140
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    remind_date = models.DateTimeField(
        auto_now=False, 
        auto_now_add=False
    )
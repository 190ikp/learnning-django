from django.db import models

class Post(models.Model):
    WHEN_REMIND = (
        (1, '15min before'),
        (2, '30min before'),
        (3, '1h before'),
    )
    title = models.CharField(max_length=20)
    content = models.TextField()
    deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    when_remind = models.IntegerField(choices=WHEN_REMIND)
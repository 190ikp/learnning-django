from django.db import models

class Post(models.Model):
    WHEN_REMIND = (
        (1, '15分前'),
        (2, '30分前'),
        (3, '1時間前'),
        (4, '3時間前'),
    )
    title = models.CharField(max_length=20)
    content = models.TextField()
    deadline = models.DateTimeField()
    when_remind = models.IntegerField(choices=WHEN_REMIND)

    def __str__(self):
        return self.title
from django.db import models
import datetime

class Post(models.Model):
    WHEN_REMIND = (
        (1, '15分前'),
        (2, '30分前'),
        (3, '1時間前'),
        (4, '3時間前'),
    )
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    deadline = models.DateTimeField()
    when_remind = models.IntegerField(choices=WHEN_REMIND)

    def __str__(self):
        return self.title
    
    def remind(self):
        if self.when_remind == 1:
            remind_before = datetime.timedelta(minutes=15)
        elif self.when_remind == 2:
            remind_before = datetime.timedelta(minutes=30)
        elif self.when_remind == 3:
            remind_before = datetime.timedelta(hours=1)
        elif self.when_remind == 4:
            remind_before = datetime.timedelta(hours=3)
        
        return(self.deadline - remind_before)
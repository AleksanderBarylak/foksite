from django.db import models
from datetime import datetime

# Create your models here.
class Msg(models.Model):
    msg_author_username = models.CharField(max_length=35)
    msg_content = models.TextField()
    msg_send_time = models.DateTimeField("sended", default = datetime.now())

    def __str__(self):
        n1 = '\n'
        return f"Msg by {self.msg_author_username}{n1}{self.msg_send_time}"

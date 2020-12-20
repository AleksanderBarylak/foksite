from django.db import models

# Create your models here.
class Msg(models.Model):
    msg_author_username = models.CharField(max_length=35)
    msg_content = models.TextField()
    msg_send_time = models.DateTimeField("sended")

    def __str__(self):
        n1 = '\n'
        return f"{self.msg_author_username}{n1}{self.msg_content}{n1}{self.msg_send_time}"

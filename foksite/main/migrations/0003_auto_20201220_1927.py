# Generated by Django 3.1.4 on 2020-12-20 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201220_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='msg_send_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 20, 19, 27, 39, 992464), verbose_name='sended'),
        ),
    ]

# Generated by Django 2.0.1 on 2018-11-04 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0005_chat_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='ddabong',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chat',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 4, 16, 53, 24, 548678)),
        ),
    ]

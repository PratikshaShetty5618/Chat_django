# Generated by Django 2.1.7 on 2020-02-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatsystem', '0002_chats_time_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='art_id',
            field=models.IntegerField(default=0),
        ),
    ]

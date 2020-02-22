# Generated by Django 2.1.7 on 2020-02-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='base_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auction',
            name='owner',
            field=models.CharField(default='XYZ', max_length=42),
        ),
    ]

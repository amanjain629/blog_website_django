# Generated by Django 3.2.4 on 2021-06-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="My freakin' awesome blog", max_length=255),
        ),
    ]

# Generated by Django 4.1.3 on 2023-06-25 17:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainPoll', '0002_alter_poll_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='voters',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
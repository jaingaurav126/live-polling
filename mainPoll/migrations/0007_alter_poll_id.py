# Generated by Django 4.2.1 on 2023-06-28 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPoll', '0006_alter_poll_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='id',
            field=models.CharField(default='poll-88212018', editable=False,
                                   max_length=50, primary_key=True, serialize=False),
        ),
    ]

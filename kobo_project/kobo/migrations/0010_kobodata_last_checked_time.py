# Generated by Django 2.0.5 on 2018-05-31 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobo', '0009_auto_20180521_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='kobodata',
            name='last_checked_time',
            field=models.DateTimeField(null=True),
        ),
    ]

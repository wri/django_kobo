# Generated by Django 2.0.5 on 2018-05-10 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kobo', '0005_auto_20180510_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='last_update_time',
            field=models.DateTimeField(null=True),
        ),
    ]

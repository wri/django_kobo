# Generated by Django 2.0.5 on 2018-05-23 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bns', '0010_auto_20180522_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answergs',
            name='price',
        ),
        migrations.AlterUniqueTogether(
            name='answergs',
            unique_together={('answer', 'gs')},
        ),
    ]

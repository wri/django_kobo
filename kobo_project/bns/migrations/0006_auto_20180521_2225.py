# Generated by Django 2.0.5 on 2018-05-21 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bns', '0005_auto_20180521_2222'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='answer',
            name='dataset_id',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='dataset_name',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='dataset_owner',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='dataset_year',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='row_id',
        ),
    ]

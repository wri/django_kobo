# Generated by Django 2.1.3 on 2018-11-07 21:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nrgt', '0003_nrgt_form_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='NRGTForm',
            fields=[
                ('dataset_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dataset_name', models.TextField(blank=True, null=True)),
                ('dataset_year', models.TextField(blank=True, null=True)),
                ('dataset_owner', models.TextField(blank=True, null=True)),
                ('dataset_uuid', models.TextField(blank=True, null=True)),
                ('last_submission_time', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('last_update_time', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('last_checked_time', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('kobo_managed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'NRGT Form',
                'verbose_name_plural': 'NRGT Forms',
                'db_table': 'nrgt_form',
                'managed': False,
            },
        ),
    ]

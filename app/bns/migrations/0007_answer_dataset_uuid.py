# Generated by Django 2.0.5 on 2018-05-22 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kobo', '0009_auto_20180521_2222'),
        ('bns', '0006_auto_20180521_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='dataset_uuid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kobo.Connection'),
            preserve_default=False,
        ),
    ]
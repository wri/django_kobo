# Generated by Django 2.0.5 on 2018-05-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bns', '0008_auto_20180522_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answergps',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='answergps',
            name='long',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=6, null=True),
        ),
    ]

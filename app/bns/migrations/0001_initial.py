# Generated by Django 2.0.5 on 2018-05-07 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AME',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(max_length=255)),
                ('ame', models.FloatField(blank=True, null=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answer_id', models.UUIDField(primary_key=True, serialize=False)),
                ('dataset_id', models.BigIntegerField()),
                ('dataset_name', models.TextField(blank=True, null=True)),
                ('dataset_owner', models.TextField(blank=True, null=True)),
                ('dataset_year', models.FloatField(blank=True, null=True)),
                ('row_id', models.BigIntegerField()),
                ('landscape', models.CharField(blank=True, max_length=255, null=True)),
                ('surveyor', models.CharField(blank=True, max_length=255, null=True)),
                ('participant', models.CharField(blank=True, max_length=255, null=True)),
                ('arrival', models.IntegerField(blank=True, null=True)),
                ('district', models.CharField(blank=True, max_length=255, null=True)),
                ('village', models.CharField(blank=True, max_length=255, null=True)),
                ('hh_type_control', models.NullBooleanField()),
                ('hh_type_org_benef', models.NullBooleanField()),
                ('hh_type_other_benef', models.NullBooleanField()),
                ('hh_id', models.CharField(blank=True, max_length=255, null=True)),
                ('livelihood_1', models.CharField(blank=True, max_length=255, null=True)),
                ('livelihood_2', models.CharField(blank=True, max_length=255, null=True)),
                ('livelihood_3', models.CharField(blank=True, max_length=255, null=True)),
                ('livelihood_4', models.CharField(blank=True, max_length=255, null=True)),
                ('benef_project', models.NullBooleanField()),
                ('explain_project', models.CharField(blank=True, max_length=255, null=True)),
                ('know_pa', models.NullBooleanField()),
                ('benef_pa', models.NullBooleanField()),
                ('explain_benef_pa', models.CharField(blank=True, max_length=255, null=True)),
                ('bns_plus', models.CharField(blank=True, max_length=255, null=True)),
                ('survey_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerGPS',
            fields=[
                ('instace_id', models.UUIDField(primary_key=True, serialize=False)),
                ('lat', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('long', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('geom', models.TextField(blank=True, null=True)),
                ('answer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bns.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerGS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gs', models.TextField()),
                ('necessary', models.NullBooleanField()),
                ('have', models.NullBooleanField()),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=1000, max_digits=1000, null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bns.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerHHMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.TextField(blank=True, null=True)),
                ('birth', models.IntegerField(blank=True, null=True)),
                ('ethnicity', models.TextField(blank=True, null=True)),
                ('head', models.NullBooleanField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bns.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerNR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr', models.TextField()),
                ('nr_collect', models.IntegerField(blank=True, null=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bns.Answer')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('dataset_id', 'row_id')},
        ),
        migrations.AlterUniqueTogether(
            name='ame',
            unique_together={('age', 'gender')},
        ),
    ]

# Generated by Django 2.0.1 on 2018-01-28 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('name', models.TextField(max_length=500)),
                ('uid', models.CharField(max_length=500)),
                ('quesid', models.IntegerField()),
                ('aid', models.CharField(max_length=500)),
                ('voting', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('name', models.TextField(max_length=500)),
                ('uid', models.CharField(max_length=500)),
                ('qid', models.IntegerField(primary_key=True, serialize=False)),
                ('boolValue', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('uid', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('userId', models.IntegerField()),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
    ]

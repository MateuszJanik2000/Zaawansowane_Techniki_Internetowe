# Generated by Django 3.1.4 on 2020-12-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='picture_url',
            field=models.CharField(default='', max_length=2083),
        ),
    ]

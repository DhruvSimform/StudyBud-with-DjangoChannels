# Generated by Django 3.2.15 on 2022-08-12 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20220812_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='connections_count',
            field=models.IntegerField(default=0),
        ),
    ]

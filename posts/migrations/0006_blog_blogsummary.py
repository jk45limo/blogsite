# Generated by Django 3.0.6 on 2020-05-21 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200521_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogsummary',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]

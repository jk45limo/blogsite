# Generated by Django 3.0.5 on 2020-04-30 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200429_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='draft',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]

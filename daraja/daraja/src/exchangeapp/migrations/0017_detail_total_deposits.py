# Generated by Django 3.1.1 on 2021-05-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0016_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='total_deposits',
            field=models.IntegerField(default=0),
        ),
    ]

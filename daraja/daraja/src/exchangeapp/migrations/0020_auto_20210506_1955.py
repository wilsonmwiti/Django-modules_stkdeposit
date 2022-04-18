# Generated by Django 3.1.1 on 2021-05-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0019_detail_inviter_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='link',
        ),
        migrations.AlterField(
            model_name='detail',
            name='inviter_link',
            field=models.CharField(default='none', max_length=30),
        ),
        migrations.AlterField(
            model_name='detail',
            name='inviter_phone',
            field=models.CharField(default='none', max_length=30),
        ),
    ]
# Generated by Django 3.1.1 on 2021-04-03 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exchangeapp', '0008_auto_20210403_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active_share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='none', max_length=30)),
                ('shares_amount', models.IntegerField(default=0)),
                ('shares_value', models.IntegerField(default=0)),
                ('profit', models.IntegerField(default=0)),
                ('code', models.IntegerField(default=0)),
                ('period', models.CharField(default='none', max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('detail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exchangeapp.detail')),
            ],
        ),
    ]

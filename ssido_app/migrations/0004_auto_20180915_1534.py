# Generated by Django 2.1.1 on 2018-09-15 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssido_app', '0003_auto_20180908_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user_id',
            field=models.CharField(default='unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='member',
            name='user_psw',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]

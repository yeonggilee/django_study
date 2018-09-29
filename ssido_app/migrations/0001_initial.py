# Generated by Django 2.1.1 on 2018-09-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=50)),
                ('age', models.IntegerField(default='20')),
                ('phone', models.CharField(default='010-0000-0000', max_length=50)),
            ],
        ),
    ]

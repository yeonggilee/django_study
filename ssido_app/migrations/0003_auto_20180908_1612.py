# Generated by Django 2.1.1 on 2018-09-08 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssido_app', '0002_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Test',
            new_name='BestFood',
        ),
        migrations.RenameField(
            model_name='bestfood',
            old_name='best_food',
            new_name='food_name',
        ),
    ]
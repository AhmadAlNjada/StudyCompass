# Generated by Django 4.0.3 on 2022-03-20 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userProgress',
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.IntegerField(max_length=10, primary_key=True, serialize=False),
        ),
    ]

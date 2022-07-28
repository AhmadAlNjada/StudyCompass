# Generated by Django 4.0.3 on 2022-03-22 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_instructor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseLink', models.TextField()),
                ('coursetitle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
    ]

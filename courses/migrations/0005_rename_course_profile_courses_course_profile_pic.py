# Generated by Django 3.2.6 on 2021-09-07 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_courses_course_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='course_profile',
            new_name='course_profile_pic',
        ),
    ]

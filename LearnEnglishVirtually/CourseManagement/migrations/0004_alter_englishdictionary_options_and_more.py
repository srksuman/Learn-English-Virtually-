# Generated by Django 4.0.1 on 2022-02-04 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseManagement', '0003_englishfacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='englishdictionary',
            options={'verbose_name_plural': 'English Dictionary'},
        ),
        migrations.AlterModelOptions(
            name='englishfacts',
            options={'verbose_name_plural': 'English Facts'},
        ),
        migrations.AlterModelOptions(
            name='maincontent',
            options={'verbose_name_plural': 'Course Contents'},
        ),
    ]

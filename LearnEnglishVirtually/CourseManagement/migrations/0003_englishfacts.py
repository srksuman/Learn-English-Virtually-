# Generated by Django 4.0.1 on 2022-02-04 01:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseManagement', '0002_englishdictionary'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishFacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
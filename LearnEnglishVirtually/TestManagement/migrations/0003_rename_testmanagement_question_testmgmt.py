# Generated by Django 4.0.1 on 2022-02-03 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestManagement', '0002_alter_testmanagement_required_score_to_pass'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='TestManagement',
            new_name='TestMgmt',
        ),
    ]

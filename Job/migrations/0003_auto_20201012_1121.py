# Generated by Django 3.1.2 on 2020-10-12 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0002_auto_20201012_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='experinc',
            new_name='experience',
        ),
    ]
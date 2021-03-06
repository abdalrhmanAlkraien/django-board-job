# Generated by Django 3.1.2 on 2020-10-12 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='experinc',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=15),
        ),
    ]

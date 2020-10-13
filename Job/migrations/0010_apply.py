# Generated by Django 3.1.2 on 2020-10-13 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0009_auto_20201013_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('converletter', models.TextField(max_length=500)),
            ],
        ),
    ]

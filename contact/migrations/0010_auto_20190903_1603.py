# Generated by Django 2.2.4 on 2019-09-03 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20190821_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='doctor',
        ),
        migrations.AddField(
            model_name='patients',
            name='doctor',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='patients',
            name='test',
        ),
        migrations.AddField(
            model_name='patients',
            name='test',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
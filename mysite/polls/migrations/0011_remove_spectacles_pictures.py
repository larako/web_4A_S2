# Generated by Django 2.0.dev20170317160306 on 2017-04-01 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20170401_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spectacles',
            name='pictures',
        ),
    ]

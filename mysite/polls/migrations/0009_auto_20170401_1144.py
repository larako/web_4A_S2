# Generated by Django 2.0.dev20170317160306 on 2017-04-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20170329_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spectacles',
            name='pictures',
            field=models.ImageField(upload_to='static/'),
        ),
    ]

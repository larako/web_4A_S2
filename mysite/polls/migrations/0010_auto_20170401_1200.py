# Generated by Django 2.0.dev20170317160306 on 2017-04-01 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20170401_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spectacles',
            name='pictures',
            field=models.ImageField(upload_to=''),
        ),
    ]

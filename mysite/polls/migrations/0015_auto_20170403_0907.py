# Generated by Django 2.0.dev20170402012442 on 2017-04-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20170401_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spectacles',
            old_name='date',
            new_name='beginningdate',
        ),
        migrations.AddField(
            model_name='spectacles',
            name='endingdate',
            field=models.DateField(blank='True', null='True'),
        ),
    ]

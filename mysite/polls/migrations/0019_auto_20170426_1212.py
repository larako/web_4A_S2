# Generated by Django 2.0.dev20170317160306 on 2017-04-26 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20170425_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='ressource',
        ),
        migrations.AddField(
            model_name='purchase',
            name='Spectacles',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.Spectacles'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchaser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

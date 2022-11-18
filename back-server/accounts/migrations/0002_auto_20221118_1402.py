# Generated by Django 3.2.13 on 2022-11-18 05:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='platform_subscribe',
            field=models.JSONField(default=dict, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]

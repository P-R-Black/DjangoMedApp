# Generated by Django 4.1.4 on 2022-12-23 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0008_usersession_delete_userhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='name',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='meditation.soundscape'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0010_rename_name_usersession_song_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersession',
            name='song_name',
            field=models.CharField(max_length=150),
        ),
    ]
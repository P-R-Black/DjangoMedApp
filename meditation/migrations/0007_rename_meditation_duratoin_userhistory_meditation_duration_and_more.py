# Generated by Django 4.1.4 on 2022-12-20 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0006_category_mood'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userhistory',
            old_name='meditation_duratoin',
            new_name='meditation_duration',
        ),
        migrations.RenameField(
            model_name='userhistory',
            old_name='user',
            new_name='name',
        ),
    ]
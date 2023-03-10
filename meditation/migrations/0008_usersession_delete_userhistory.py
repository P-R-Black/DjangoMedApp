# Generated by Django 4.1.4 on 2022-12-22 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meditation', '0007_rename_meditation_duratoin_userhistory_meditation_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_meditation', models.DateTimeField(auto_now_add=True)),
                ('moods_before_meditation', models.CharField(max_length=25, null=True)),
                ('meditation_duration', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UserHistory',
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meditation', '0014_remove_mood_category_mood_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mood',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='moods',
            field=models.ManyToManyField(to='meditation.mood'),
        ),
    ]

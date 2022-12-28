from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Soundscape(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    meditation_sounds = models.FileField(upload_to='med_sounds/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cs50_meditation:med_sounds', args=[self.id, self.slug])


class StopStartSounds(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    start_and_stop_sounds = models.FileField(upload_to='start_stop_sounds')


class UserSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_meditation = models.DateTimeField(auto_now_add=True)
    moods_before_meditation = models.CharField(max_length=25, null=True)
    meditation_duration = models.CharField(max_length=20)
    song_name = models.CharField(max_length=150)


class Category(models.Model):
    major_mood = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.major_mood


class Mood(models.Model):
    mood = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.mood

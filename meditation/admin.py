from django.contrib import admin
#from .models import Patronus, Soundscape, UserHistory
from django.contrib.auth.models import User

from .models import Soundscape, StopStartSounds, Category, Mood


# Register your models here.
# admin.site.register(Patronus)

# @admin.register(User)

# @admin.register)
class UserProfile:
    list_display = ['date_of_birth']


@admin.register(Soundscape)
class Sounds(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']


@admin.register(StopStartSounds)
class IntervalSounds(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['major_mood', 'slug']

    def get_prepoplulated_fields(self, request, obj=None):
        return {'slug': ('major_mood',)}


@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ['mood', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('mood',)}

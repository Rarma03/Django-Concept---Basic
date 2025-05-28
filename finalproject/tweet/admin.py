from django.contrib import admin
from .models import Tweet

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    # list_display = ('user', 'text')     # normal

    list_display = ('user','user_email','text') # we want to display user email from user model also
    def user_email(self, obj):
        return obj.user.email
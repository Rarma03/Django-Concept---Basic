# In forms generall 2 cheeze hmesha import hogi 1. forms & 2. defined models

from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
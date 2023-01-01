from .models import Tweet
from django import forms


class CreateTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
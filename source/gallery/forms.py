from django import forms
from django import forms
from django.forms.widgets import Textarea, HiddenInput, Input

from gallery.models import Photography


class PostForm(forms.ModelForm):
    class Meta:
        model = Photography
        fields = ('description', 'photo')

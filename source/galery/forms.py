from django import forms
from django import forms
from django.forms.widgets import Textarea, HiddenInput, Input

from galery.models import Photography


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photography
        fields = ('description', 'photo')

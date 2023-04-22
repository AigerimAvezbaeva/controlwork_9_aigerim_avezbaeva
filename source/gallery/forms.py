from django import forms
from django import forms
from django.forms.widgets import Textarea, HiddenInput, Input

from gallery.models import Photography


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photography
        fields = ('description', 'photo')

    def save(self, commit=True):
        object = super().save(commit=False)
        photo = self.cleaned_data.get('photo')
        if photo:
            object.photo = photo
        if commit:
            object.save()
        return object

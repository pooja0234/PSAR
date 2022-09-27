from django import forms

from . models import Allpost


class Edit_Blog(forms.ModelForm):
    class Meta:
        model = Allpost
        fields = ('title', 'images', 'content')

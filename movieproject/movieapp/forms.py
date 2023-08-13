from django import forms
from .models import Movie

class mform(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','year','img']
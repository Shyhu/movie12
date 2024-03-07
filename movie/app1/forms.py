from django import forms
from app1.models import Movie
class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','year','img']
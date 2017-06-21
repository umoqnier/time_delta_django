from django import forms
from django.forms import ModelForm

class DateForm(forms.Form):
    date_1 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "input-field col s6",
                "placeholder": "Day dd Mon yyyy hh:mm:ss +xxxx"
            }
        )
    )
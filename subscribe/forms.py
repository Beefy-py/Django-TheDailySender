from django import forms
from .get_all_countries import ALL_COUNTRIES


class SubscribeForm(forms.Form):
    name = forms.CharField(max_length=50, label='Nickname')
    email = forms.EmailField(max_length=100)
    country = forms.ChoiceField(choices=ALL_COUNTRIES)


class UnsubscribeForm(forms.Form):
    email = forms.EmailField(max_length=100, label='Enter Your Email')

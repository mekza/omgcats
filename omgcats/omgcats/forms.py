from django import forms


class MyFirstForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')

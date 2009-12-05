from django import forms


class ExampleForm(forms.Form):
    foo = forms.CharField()

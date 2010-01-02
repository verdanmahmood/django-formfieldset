from django import forms
from formfieldset.forms import FieldsetMixin


class ExampleForm(forms.Form, FieldsetMixin):
    """A fancy registration form"""
    fieldsets = (
        (u'Avatar Info', {'fields': ('avatar_name', 'avatar_gender')}),
        (u'Account Info', {'fields': ('first_name',
                                      'last_name',
                                      'username',
                                      'email',
                                      'password',
                                      'password_again')}),
    )

    avatar_name = forms.CharField()
    avatar_gender = forms.ChoiceField(choices=(('F', u'Female'),
                                               ('M', u'Male')))
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_again = forms.CharField(widget=forms.PasswordInput)

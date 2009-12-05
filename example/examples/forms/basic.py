from django import forms
from formfieldset.forms import FieldsetMixin


class ExampleForm(forms.Form, FieldsetMixin):
    """Your basic contact form"""
    fieldsets = (
        (u'Personal Info', {'fields': ('your_name',
                                       'email_address',
                                       'homepage')}),
        (u'Message', {'fields': ('your_message',)}),
        (u'Options', {'fields': ('send_a_copy_to_me',)}),
    )

    your_name = forms.CharField()
    email_address = forms.EmailField()
    homepage = forms.URLField()
    your_message = forms.CharField(widget=forms.widgets.Textarea)
    send_a_copy_to_me = forms.BooleanField()

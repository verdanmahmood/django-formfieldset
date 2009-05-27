from django import forms
from formfieldset.forms import FieldsetMixin


class ContactForm(forms.Form, FieldsetMixin):
    full_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    website = forms.URLField()
    message = forms.CharField(max_length=500, widget=forms.Textarea)
    send_notification = forms.BooleanField(required=False)

    fieldsets = ((u'Personal Information',
                  {'fields': ('full_name', 'email', 'website'),
                   'description': u'Your personal information will not ' \
                                  u'be shared with 3rd parties.'}),
                 (None,
                  {'fields': ('message',),
                   'description': u'All HTML will be stripped out.'}),
                 (u'Preferences',
                  {'fields': ('send_notification',)}))
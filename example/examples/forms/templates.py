from django import forms
from formfieldset.forms import FieldsetMixin


class ExampleForm(forms.Form, FieldsetMixin):
    """Your basic contact form... with custom fieldset templates"""
    fieldsets = (
        (u'Personal Info', {'fields': ('your_name',
                                       'email_address',
                                       'homepage')}),
        (u'Message', {'fields': ('your_message',)}),
        (u'Options', {'fields': ('send_a_copy_to_me',)}),
    )

    _tmpl_table = (
        u'<fieldset>%(title)s<table>%(fields)s</table></fieldset>',
        u'<legend>%s</legend>',
        u'%s',
        u'<tr><th>%(label)s</th><td>%(errors)s' \
                                          u'%(field)s%(help_text)s</td></tr>',
        u'<tr><td colspan="2">%s</td></tr>',
        u'</td></tr>',
        u'<br />%s',
        False,
    )

    your_name = forms.CharField()
    email_address = forms.EmailField()
    homepage = forms.URLField()
    your_message = forms.CharField(widget=forms.widgets.Textarea)
    send_a_copy_to_me = forms.BooleanField()
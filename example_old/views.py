import os
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
import forms

def example(request, example_name):
    forms_py_path = os.path.join(os.path.dirname(forms.__file__), 'forms.py')
    ctx = {'forms_py': open(forms_py_path, 'rb').read(),
           'form': forms.ContactForm()}
    return render_to_response('example/%s.html' % example_name,
                              RequestContext(request, ctx))
import os
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
import forms

def homepage(request):
    forms_py_path = os.path.join(os.path.dirname(forms.__file__), 'forms.py')
    ctx = {'forms_py': open(forms_py_path, 'rb').read(),
           'form': forms.ContactForm()}
    return render_to_response('example/index.html',
                              RequestContext(request, ctx))
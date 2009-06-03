# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name = 'django-formfieldset',
    version = '1.0.0',
    url = 'http://github.com/muhuk/django-formfieldset/tree/master',
    author = 'Atamert Ölçgen',
    author_email = 'muhuk@muhuk.com',
    license = 'BSD',
    packages = ['formfieldset'],
    description = 'Fieldset Rendering For Non-Admin Forms',
    classifiers = ['Development Status :: 5 - Production/Stable',
                    'Environment :: Web Environment',
                    'Framework :: Django',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: BSD License',
                    'Topic :: Internet :: WWW/HTTP :: Dynamic Content']
)

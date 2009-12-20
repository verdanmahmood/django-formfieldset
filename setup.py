from distutils.core import setup
from formfieldset import __version__, __maintainer__, __email__


license_text = open('LICENSE.txt').read()
long_description = open('README.rst').read()


setup(
    name = 'django-formfieldset',
    version = __version__,
    url = 'http://github.com/muhuk/django-formfieldset/tree/master',
    author = __maintainer__.encode('utf8'),
    author_email = __email__,
    license = license_text,
    packages = ['formfieldset'],
    description = 'Fieldset Rendering For Non-Admin Forms',
    long_description=long_description,
    classifiers = ['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Topic :: Internet :: WWW/HTTP :: Dynamic Content']
)

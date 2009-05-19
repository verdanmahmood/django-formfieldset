import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'

ROOT_URLCONF = 'example.urls'

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
)

INSTALLED_APPS = (
    'formfieldset',
)

SECRET_KEY = '#s$zy-6goa)#&bn5)z!)ky+=295(x)pj!_p34n(1z_8_xm55no'
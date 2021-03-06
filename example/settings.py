import os


_PATH = os.path.abspath(os.path.dirname(__file__))
_MODULE = os.path.basename(_PATH)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'

ROOT_URLCONF = _MODULE + '.urls'

MEDIA_ROOT = os.path.join(_PATH, 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_DIRS = (
    os.path.join(_PATH, 'templates'),
)

INSTALLED_APPS = (
    'formfieldset',
    'examples',
)

SECRET_KEY = '#s$zy-6goa)#&bn5)z!)ky+=295(x)pj!_p34n(1z_8_xm55no'

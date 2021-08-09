from .base import *

ALLOWED_HOSTS = ['18.142.86.108', 'bsvproduction.com']
STATIC_ROOT = BASE_DIR / 'static/'
STATICFILES_DIRS = []
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'om',
        'USER': 'dbmasteruser',
        'PASSWORD': '+rZ#Gj86nv;`JM)%bxF:,r2a9!EzYgCK',
        'HOST': 'ls-c10cd64e6234e3777557784bcf18989ef78c04c0.clgqotdraprx.ap-southeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
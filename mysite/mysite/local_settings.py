import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mysite_django',
        'USER': 'postgres',
        'PASSWORD': 'matrix',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

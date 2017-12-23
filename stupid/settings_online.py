# -*- coding: utf-8 -*-
from stupid.settings import location

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': location('db.sqlite3'),
    }
}

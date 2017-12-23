# -*- coding: utf-8 -*-
__author__ = 'ziven'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'OPTIONS': {'charset': 'utf8mb4'},
        'NAME': 'jpmedical_dev',  # Or path to database file if using sqlite3.
        'USER': 'jpmedical',  # Not used with sqlite3.
        'PASSWORD': 'zky@af616',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
        'CONN_MAX_AGE': 3600
    }
}

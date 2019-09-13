#!/bin/sh

if [ "$1" = 'local' ]; then
    python manage.py bootstrap
    python manage.py runserver 0:8000
fi

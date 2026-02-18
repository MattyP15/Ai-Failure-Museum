#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python 4_code/djangoCode/manage.py collectstatic --no-input

python 4_code/djangoCode/manage.py migrate
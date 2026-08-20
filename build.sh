#!/usr/bin/env bash
# Exit on error
set -o errexit

pip install -r requirements.txt

# Navigate into the inner bookstore folder where manage.py is located
cd bookstore

python manage.py collectstatic --no-input
python manage.py migrate
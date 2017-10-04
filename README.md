# django_site

virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate

python3 manage.py runserver


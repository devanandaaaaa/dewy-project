
set -e  

pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata initial_data_cleaned.json
python manage.py collectstatic --noinput

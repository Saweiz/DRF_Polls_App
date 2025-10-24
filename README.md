# Polls App using Django Rest Framework

Note: You need to have `python`, and `virtualenv` module installed on your machine.

### Quick Start

Create and Activate a virtual environment
```bash
python -m venv venv
source ./venv/bin/activate
```

Install dependencies from requirements.txt file
```bash
pip install -r requirements.txt
```

Create Super User
```bash
python manage.py createsuperuser
```

Migrate database tables
```bash
python manage.py makemigrations
python manage.py migrate
```

Run the application
```bash
python manage.py runserver
```
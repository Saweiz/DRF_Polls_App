# Polls App using Django Rest Framework

Note: You need to have `python`, and `virtualenv` module installed on your machine.

### Quick Start

Clone the Repository and Navigate to project directory
```bash
git clone git@github.com:Saweiz/DRF_Polls_App.git
cd DRF_Polls_App/
```

Create and Activate a virtual environment
```bash
python -m venv venv
source ./venv/bin/activate
```

Install dependencies from requirements.txt file
```bash
pip install -r requirements.txt
```

Migrate database tables
```bash
python manage.py makemigrations
python manage.py migrate
```

Create Super User
```bash
python manage.py createsuperuser
```

Run the application
```bash
python manage.py runserver
```
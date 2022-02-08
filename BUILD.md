
### Setup Python Virtual Environment

We create a python virtual environment at the top level directory. Each subdirectory can be a separate python application but they all use the same environment.

1. Create venv `python3 -m venv venv`
1. Activate venv `source ./venv/bin/activate`
1. Upgrade pip `pip install --upgrade pip`
1. Install dependencies `pip install -r requirements.txt`

### Build

1. Activate venv `source ./venv/bin/activate`
1. Run migrations `python manage.py migrate`
1. Create superupser for admin interface `python manage.py createsuperuser`
1. Load Data into the database from the CSV files `python manage.py load_csv`.
1. Create directory `ccgg/static/ccgg`
1. Generate graphs `python manage.py generate_graph` to generate average and 
1. Start Development Webserver `python manage.py runserver 22320`

### Test Cases - `ccgg/`

1. _ACC-CCGG-001_ Given browser is started when I go to the home page then I see two graphs

### Test Cases - `admin/`

1. _ACC-ADMIN-001_ Given browser is started when I go to the admin page then I data from the CSV file.

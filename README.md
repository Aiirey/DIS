TODO: Take inspiration from others.

## Requirements:
Run the code below to install the necessary modules.

    pip install -r requirements.txt

For WINDOWS: Loading data into Postgres using psql needs to explicitly use UTF-8 by executing this command:

    set PGCLIENTENCODING=UTF8

## Database init
1. set the database in __init__.py file.
2. run schema.sql in your database

Example: 

    psql -d{database} -U{user} -W -f schema.sql
   
#### notes
For Ubuntu add host (-h127.0.0.1) to psql: 

    psql -d{database} -U{user} -h127.0.0.1 -W -f schema.sql

## Running flask
### The python way

    python3 run.py

### The flask way.

    export FLASK_APP=run.py
    export FLASK_DEBUG=1           (Replaces export FLASK_ENV=development)
    export FLASK_RUN_PORT=5004     (Optional if you want to change port numbe4. Default port is port 5000.)
    flask run

#### notes
For Windows you may have to use the SET command instead of EXPORT. Ex set FLASK_APP=run.py; set FLASK_DEBUG=1; flask run. This worked for me. Also remeber to add the path to your postgres bin-directory in order to run (SQL interpreter) and other postgres programs in any shell.

Projekt: Inovace zpravodajského storytellingu C


# Newschatbot backend

Python Flask REST API application to support Chatfuels Chatbot. Deployment is done with Serverless Framework to AWS Lambda. Application is connected to Postgres database.

## Init setup
Python  setup
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Database setup
```
cd dockers/postgres/
docker-compose up

set FLASK_APP=app/main:app;
flask db upgrade
```
Flask application is run from app/main.py

### Database migration
Creates a migration repository
```
flask db init 
```
Generates migration file based on the model.
```
flask db migrate
```
Performs migration in the db.
```
flask db update
```

### Serverless deployment
Node setup
```
npm ci
```

## Contributing
### Before pushing changes
Before you push your changes, run code formatter Black by using the following command:
```
black {source_file_or_directory} 
```
If the script doesn't work, run Black as package: 
```
python3 -m black {source_file_or_directory}
```
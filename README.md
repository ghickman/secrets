# Secrets
Every application has it's own secrets these days, be it database passwords or AWS credentials, they've all got them somewhere. Secrets aims to provide a place to securely store your application's configuration options with a REST API on top.

## Deployment
Clone the repository:

    git clone git://github.com/ghickman/secrets.git

Create the heroku app:

    heroku create --stack cedar

Set your AWS variables:

    heroku config:add AWS_ACCESS_KEY_ID=<secret key>
    heroku config:add AWS_SECRET_ACCESS_KEY=<secret access key>
    heroku config:add AWS_STORAGE_BUCKET_NAME=<bucket name>

Push up to Heroku:

    git push heroku master

Create the database:

    heroku run python manage.py syncdb

Add some users!


## API
**Endpoint**: `/api/<application>`

### Create
Accepts: POST

    {'application_name': [
        {''},
        {},
    ]}

### Read
Accepts: GET

### Example

    import requests

    password = 'secret'
    user = 'me'

    r = requests.get('http://secrets.awesome.tld/api/awesome_app', auth=(user, password))
    print r
    # {'application_name': [
    #     {'database_name': 'database'},
    #     {'database_password': 'secret'}
    #     {'AWS_SECRET_KEY_ID': 'secret'},
    #     {'AWS_SECRET_ACCESS_KEY': 'secret'},
    #     {'AWS_STORAGE_BUCKET': 'secret'},
    # ]}


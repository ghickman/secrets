# Secrets

Secrets is a Django application for hosting your private runtime settings in a central database. Settings such as SECRET_KEY or AWS login information can be kept secure, and retrived via a REST API as part of your deployment process.

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

POST to create
GET to read

### Example

    import requests

    endpoint = 'http://secrets.awesome.tld/api/awesome_app'
    password = 'secret'
    user = 'me'

    payload = {
        'application_name': [
            {'database_name': 'database'},
            {'database_password': 'secret'}
            {'AWS_SECRET_KEY_ID': 'secret'},
            {'AWS_SECRET_ACCESS_KEY': 'secret'},
            {'AWS_STORAGE_BUCKET': 'secret'},
        ]
    }

    r = requests.post(endpoint, auth=(user, password), data=payload)
    print r.status_code # 201

    r = requests.get(endpoint, auth=(user, password))
    print r.status_code # 200
    print r

    # {'application_name': [
    #     {'database_name': 'database'},
    #     {'database_password': 'secret'}
    #     {'AWS_SECRET_KEY_ID': 'secret'},
    #     {'AWS_SECRET_ACCESS_KEY': 'secret'},
    #     {'AWS_STORAGE_BUCKET': 'secret'},
    # ]}


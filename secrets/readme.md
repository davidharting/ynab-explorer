# Secrets
This directory contains private credentials and environment information.

You must create files with a particular format for this to run properly.
The files are not version controlled. Each environment must provide them.

## Token

In this directory, create a file called `token.py`.

Then put the following content in it:

```python
token = "your YNAB personal access token""
```

## Database

In this directory, create a file called `database.py`.
This will contain credentials and connection information for the Postgres instance to connect to.

```python
# Define these variables according to your environment
user = ''
password = ''
host = '' # Probably localhost
db_name = '' # Probably ynab
connection_url = 'postgres://{}:{}@{}/{}'.format(user, password, host, db_name)
```

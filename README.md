# bookshelf-api
REST API with Django

[![CircleCI](https://circleci.com/gh/erickbogarin/bookshelf-api.svg?style=svg)](https://circleci.com/gh/erickbogarin/bookshelf-api)

## Features

* Search and browse through books, authors and categories
* Sign in / Sign up (Token-Based Authentication)

## Technology Stack

* Django 1.11
* Django REST Framework
* Heroku fully cloud deployable
* Integration tests

## To Do

- [ ] Documentation of API endpoints
- [ ] Create unit tests
- [ ] Setup docker to simplify development
- [ ] Use django permissions for particular operations

## Requirement Environment

Make sure the following tools are installed and working:

- Python3, Pip3, Virtualenv (for Python3) 
- PostgresQL

## How to run this application

1. Create the database:

```bash
$ CREATE DATABASE eshopper
```

2. Create a new virtualenv

```bash
$ virtualenv venv
$ source bin/activate
```

3. Install the project packages using pip

```bash
$ pip install -Ur requirements/local.txt
```

4. Run migrations:

```bash
./manage.py migrate
```

5. Run the application:

```bash
$ ./manage.py runserver
```

## Contributing

PR's and issues welcome!

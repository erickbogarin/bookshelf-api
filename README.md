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

- [x] Documentation of API endpoints
- [x] Setup docker to simplify development
- [ ] Create unit tests
- [ ] Use django permissions for particular operations

## Requirement Environment

Make sure the following tools are installed and working:

- Python3, Pip3, Virtualenv (for Python3) 
- PostgresQL

## How to run this application

Clone this repository:


```bash
$ git clone git@github.com:erickbogarin/bookshelf-api.git
$ cd bookshelf-api
```
### Running with Docker

```bash
$ docker-compose up -d
```

Go to http://0.0.0.0:8000/ to see the app

### Manually Deploying

1. Create the database:

```bash
$ CREATE DATABASE database-name
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

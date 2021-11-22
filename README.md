# Steps to run the Bugal application containerized

1. `docker-compose build` or `docker-compose -f local.yml build`

## Django commands

### Migrations - Create/upadte DB schemas

1. `docker-compose -f local.yml  run --rm django sh -c "python manage.py makemigrations"`
2. `docker-compose -f local.yml  run --rm django sh -c "python manage.py migrate"`

### Run unit tests and linting

1. `docker-compose -f local.yml  run --rm django sh -c "python manage.py test && flake8"`
2. Specific tests can be run like this:
   `docker-compose -f local.yml  run --rm django sh -c "python manage.py test users.tests"`
   `docker-compose -f local.yml  run --rm django sh -c "python manage.py test clients.tests"`
   and so on.

### Create Superuser (Admin)

1. `docker-compose -f local.yml  run --rm django sh -c "python manage.py createsuperuser"`
   ..\* Fill up the fields (Email, First name, Last name & Password)

### Execute Django server to visualize in browser

1. `docker-compose up` or `docker-compose -f local.yml up` Executes `python manage.py runserver 0.0.0.0:8000"`
   ..\* Open browser and go to `http://localhost:8000`
   ..\* To access the admin dashboard go to `http://localhost:8000/admin`

## Docker commands

### List all the active containers

`docker ps`

### List all the containers (active and inactive)

`docker ps -qa`

### Remove all the containers

`docker rm (docker ps -qa)`

### List all the docker images

`docker images ls`

### Removes all images

`docker rmi (docker image ls | awk 'NR>1 {print \$3}')`

### List all the volumes

`docker volume ls`

### Remove all the volumes

`docker volume prune`

## API Endpoints - Sample payload

### Using Postman
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/4c26ca115a5b6b992fd7)

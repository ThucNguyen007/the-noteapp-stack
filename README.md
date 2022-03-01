# Note Application

Built using React, Python@3.10, Bootstrap, Postgres, Django, Node, and Docker.

## Requirements

- [Docker](https://www.docker.com/get-started)
- [Node](https://nodejs.org)
- [Python](https://www.python.org/downloads/)
- [React](https://reactjs.org/versions/)

## Dev

Setting Up Your Local Dev Environment.
1. Clone and cd into TodoApp3
2. Create a file named `.env` and fill in the following variables:

```
DEBUG=1
REGION=massachusetts
DJANGO_SUPERUSER_USERNAME=user1
DJANGO_SUPERUSER_PASSWORD=20Yearly22
DJANGO_SUPERUSER_EMAIL=user1@codepython.org
DJANGO_SECRET_KEY=fix_this_later

POSTGRES_READY=0
POSTGRES_DB=dockerdc
POSTGRES_PASSWORD=mysecretpassword
POSTGRES_USER=myuser
POSTGRES_HOST=localhost
POSTGRES_PORT=5435
```
2. Install [Node](https://nodejs.org) if you do not already have it.
3. Install [Yarn](https://yarnpkg.com/getting-started/install) if you do not already have it.

## Running The app.

The app can be ran using Docker. We are currently running it using a
docker-compose service.

1. Once you have the above `.env` file, navigate to your project root (right where `docker-compose.yaml` is) and run:
```
docker compose up -d
```
This will create a `postgresql` database that's running in the container. Visit [`http://localhost:8000/`](http://localhost:8000/)
in your browser to see the app and start using/developing.

2. Next you need to make migrations and migrate them to the database. To do
this, you need to first get in your docker container.
  - Run `docker ps` to list all the containers and their info.

3. When in your docker container, run the following commands. If you are on windows,use `python manage.py <command>` instad of `./manage.py`. For the migrations on windows, you may need to do list all apps explicitly.
    - Run `./manage.py makemigrations` on mac to make all the migrations.
    - If you get a message output of 'no changes detected' that is fine and you can just run the next command.
    - Run `./manage migrate` to migrate the changes.
    - More on django migrations and migrate [here](https://docs.djangoproject.com/en/1.11/topics/migrations/).
    - Whenever you make a change to your models, please repeat steps 2 and 3.

4. To bring this database down just run:
```
docker compose down
```
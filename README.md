# EconoMe Backend

Backend for the EconoMe Project. This is just a simple API that allows users to create and manage their own budgets.

I built this to familiarize myself with Python and to learn more about FastAPI.

The project uses FastAPI for the API, SQLAlchemy for the ORM, and Alembic for database migrations.

## Running Locally

In order to run the backend locally, the following must be installed only your machine

- [Python 3](https://www.python.org/downloads/)
- [pipenv](https://pypi.org/project/pipenv/) for managing dependencies
- [Docker](https://docs.docker.com/get-docker/) for running the local database

Copy the `.env.example` file to a new file called `.env` and fill in the necessary environment variables.

```shell
cp .env.example .env
```

Then run the following to install all project dependencies, including dev:

```shell
pipenv install --dev
```

Spin up the local db by running the following:

```shell
docker-compose up -d
```

You will then need to run the existing migrations to create the necessary tables in the database. To do this, navigate
to /app and then run the
following:

```shell
alembic upgrade head
```

It is also recommended to run the seed SQL scripts on the database to populate it with some initial data.
See [seeds](./seeds) for scripts.

Finally, to start the API locally, navigate back up to the root directory and run the following:

```shell
uvicorn app.main:app --reload
```

To view the API documentation, visit http://localhost:8000/docs in your browser.

### Running Locally with Docker Compose

It's a bit overkill but you can also run entire app (api and db) using docker-compose.

Uncomment the commented out section of [docker-compose.yml](docker-compose.yml) to include the app service.

Update your .env so that the db url is `postgresql://postgres:password@db:5432/postgres` so that the app can connect to
the db from within the container.

You will also need to generate a requirements.txt file as the app service will use this to install dependencies.

```shell
pipenv requirements > requirements.txt
```

Then run the following:

```shell
docker-compose up -d
```

One benefit of running the app this way is that you can guarantee that the app will run in the same environment as it
would when deployed.

Note you will still want to run the seed scripts to populate the database with initial data.

### Migrations

To create a new migration, navigate to the app directory and run the following:

```shell
alembic revision --autogenerate -m "migration message"
```

To apply the migration, run the following:

```shell
alembic upgrade head
```

### Containerization for Deployment

To build an app image, first run the following to create a requirements.txt file:

```shell
pipenv requirements > requirements.txt
```

Then build the image:

```shell
docker build -t econome-backend:version .
```

Note that `version` should be replaced with the version number of the image.

When running container images, the following environment variables must be set:

- `DATABASE_URL`
- `SECRET_KEY`
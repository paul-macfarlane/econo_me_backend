# EconoMe Backend

Backend for the EconoMe Project. This is just a simple API that allows users to create and manage their own budgets.

I built this to familiarize myself with Python and to learn more about FastAPI.

The project uses FastAPI for the API, SQLAlchemy for the ORM, and Alembic for database migrations.

## Getting Started

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

### Migrations

To create a new migration, navigate to the app directory and run the following:

```shell
alembic revision --autogenerate -m "migration message"
```

To apply the migration, run the following:

```shell
alembic upgrade head
```
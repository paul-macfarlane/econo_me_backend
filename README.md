# EconoMe Backend

Backend for the EconoMe Project.

## Getting Started

In order to run the backend locally, the following must be installed only your machine

- [Python 3](https://www.python.org/downloads/)
- [pipenv](https://pypi.org/project/pipenv/)

Then navigate to the [app directory](./app) and run the following to install all project dependencies, including dev:

```shell
pipenv install --dev
```

Finally, to start the API locally, navigate back up to the root directory and run the following:

```shell
uvicorn app.main:app --reload
```
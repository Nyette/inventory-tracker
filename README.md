# Inventory Tracker

I wanted to play with [FastAPI](https://fastapi.tiangolo.com/).

## Prerequisites

* [Python 3.9](https://www.python.org/)

* [PostgreSQL](https://www.postgresql.org/)

* [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

## Getting Started

* Clone this repo.

* Navigate to the project directory.

* [Create and activate your virtual environment.](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)

* Install packages.

`pip install -r requirements.txt`

* Add a `.env` file to the root directory of the project.

* Heroku periodically rotates credentials, so fetch and set the `DATABASE_URL` environment variable.

`dotenv set DATABASE_URL $(heroku config:get DATABASE_URL -a serene-ridge-38653)`

* Run the live server.

`uvicorn main:app --reload`

* See your changes at http://127.0.0.1:8000/.

# Log-Analysis
This project reads data from a PostgreSQL database using Python. The features are
1. Reading data from the database using Python

# Technology Used
1. Docker
2. PostgreSQL
3. Python 3

# How to run?

## Pre-requisites
1. Please make sure Python 3 is installed
4. Please make sure docker is installed


## Steps to host db

1. `git clone` the repo and `cd` into it
2. Run the below
    ```sh
    docker-compose up
    ```
3. The adminer serivice is now available in `http://localhost:8080`
4. The username is `vagrant` and password is `example` and the database name is `news`
5. You can also access the database by
    ```sh
    psql --hostname=localhost --port=5432 --username=vagrant --dbname=news
    ```
## Steps to check queries

1. Run the below to check the query output
    ```sh
    python3 db.py
    ```
2. This should give you the respective DB query outputs

License
----

MIT
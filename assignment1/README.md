#### Abstract

You will be building a simple expense mamagement system using Python Flask.

#### Prerequisites
* Docker installed on your machine.
* Create an account at [Docker hub](https://hub.docker.com/)
* Add your account to the [SJSU cmpe273 team](https://hub.docker.com/u/sjsu/dashboard/teams/?team=cmpe273). 
* See me in the class to add your account to the team.

#### APIs

> Base URL: http://localhost:5000

* POST /v1/expenses

_Request Body_

```json
{
    "name" : "Foo Bar",
    "email" : "foo@bar.com",
    "category" : "office supplies|travel|training",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "700",
    "submit_date" : "09-08-2016"
}
```
 
_Response Header_

```sh
201 Created
```

_Response Body_

```json
{
    "id" : "123456",
    "name" : "Foo Bar",
    "email" : "foo@bar.com",
    "category" : "office supplies|travel|training",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "700",
    "submit_date" : "09-08-2016",
    "status" : "pending",
    "decision_date" : "09-10-2016"
}
```

* GET /v1/expenses/{expense_id}

_Response Header_

```sh
200 OK
```

_Response Body_

```json
{
    "id" : "123456",
    "name" : "Foo Bar",
    "email" : "foo@bar.com",
    "category" : "office supplies|travel|training",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "700",
    "submit_date" : "09-08-2016",
    "status" : "pending",
    "decision_date" : "09-10-2016"
}
```

* PUT /v1/expenses/{expense_id}

_Request Body_

```json
{
    "estimated_costs" : "800"
}
```
 
_Response Header_

```sh
202 Accepted
```

* DELETE /v1/expenses/{expense_id}

 _Response Header_

```sh
204 No Content
```

#### Data Persistence

You need to store data generated from the APIs into MySQL RDBMS using [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/).


#### Docker Container Persistence

Docker provides [Data containers](https://github.com/geerlingguy/docker-examples/tree/master/flask#persisting-data) for stateful applications like Database. You will be mounting a dedicated volume for MySQL so that you can easily
manage the persistence data file generated from MySQL.

```yml
services:
  ...
  db:
    ...
    volumes:
      - ./database:/var/lib/mysql
```

See@[Another Flask MySQL Docker Example](https://github.com/geerlingguy/docker-examples/tree/master/flask)

#### Ship it in a Docker Container

* Use [Docker-compose](https://docs.docker.com/compose/) to wrap your application into a Docker container. See [this example](https://github.com/aabdulwahed/Docker-Compose/tree/master/Flask-MySQL).
* Tag your image via:

```sh
docker login
docker tag sha256:xxxxxx sjsu/your-entire-sjsu-id-assignment1
```

* Finally, you publish your image to SJSU Docker hub repository.

```sh
docker push sjsu/your-entire-sjsu-id-assignment1
```


#### Abstract

You will be building a simple expense mamagement system using Python Flask.

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
201 OK
Location: /v1/expenses/123456
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
    "status" : "pending|approved|rejected|overbudget",
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
### Abstract

In this assignment, you will be implementing client-side sharding for the expense management application that you built in the assignment 1.

### Prerequistes

* Completed the assignment 1. 
* Proxy router code from the assignment 2 should not be used in this assignment.

### Requirements

* Modify existing POST /v1/expenses endpoint so that it can take "id" as input instead of server generated id.
* Three (Docker - optional) the expense management applicaiton instances - each application instance uses its own MySQL instance.
* Three (Docker - optional) MySQL DB instances mounted to three different local paths so that each one will have different data set.

#### Consistent Hashing

* Using [this example as baseline](http://techspot.zzzeek.org/2012/07/07/the-absolutely-simplest-consistent-hashing-example/), implement Consistent hashing HTTP client that will POST new expenses (to /v1/expenses) to the above three instances. 
* You don't need to support replicas feature from the above example.
* Use __id__ as the shard key.
* Correct consistent hashing client should shard the following ten expenses into multiple back-end instances.
* Your consistent hashing client implementation will be in a file called ch_client.py in where you do the following steps:
* 1. Define three expense management applications hostnames in an array or set. E.g. nodes = {"127.0.0.1:3000", "127.0.0.1:4000", "127.0.0.1:5000"}
* 2. Implement a consistent hashing function that can take "id" as key, do all consistent hashing logic, and finally return one of the nodes from the above list.
* 3. Loop through 10 ids (0-9) and get the node mapping: "1" => "127.0.0.1:3000", "2" => "127.0.0.1:4000", etc.
* 4. Make a HTTP POST call to http://{node_returned_from_consistent_hashing_function}/v1/expenses for each id.
* 5. Loop through the same 10 ids (0-9), get the node mapping, make a HTTP GET call to  http://{node_returned_from_consistent_hashing_function}/v1/expenses/{id} for each id. If you can retrieve all ids from the right nodes using consistent hashing, then you have a correct solution.


##### Test data

_Request 1_

```json
{
    "id" : "1",
    "name" : "Foo 1",
    "email" : "foo1@bar.com",
    "category" : "office supplies",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "700",
    "submit_date" : "12-10-2016"
}
```

_Request 2_

```json
{
    "id" : "2",
    "name" : "Foo 2",
    "email" : "foo2@bar.com",
    "category" : "office supplies",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "800",
    "submit_date" : "12-10-2016"
}
```

....

_Request 10_

```json
{
    "id" : "10",
    "name" : "Foo 10",
    "email" : "foo10@bar.com",
    "category" : "office supplies",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "800",
    "submit_date" : "12-10-2016"
}
```

### NOTE 

> If you use any thrid party consistent hashing library, or random nodes or a fixed sequential order in the id-to-node mapping; you will get zero! 



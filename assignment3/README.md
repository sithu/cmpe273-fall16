### Abstract

In this assignment, you will be implementing client-side sharding for the expense management application that you built in the assignment 1.

### Prerequistes

* Completed the assignment 1.

### Requirements

* Three Docker the expense management applicaiton instances - each application instance uses one MySQL instance.
* Three Docker MySQL DB instances mounted to two different local paths so that each one will have different data set.

#### Consistent Hashing

* Using [this example as baseline](http://techspot.zzzeek.org/2012/07/07/the-absolutely-simplest-consistent-hashing-example/), implement Consistent hashing HTTP client that will POST new expenses (to /v1/expenses) to the above three instances. 
* You don't need to support replicas feature from the above example.
* Use __email__ as the shard key.
* Correct consistent hashing client should shard the following ten expenses into multiple back-end instances.


##### Test data

_Request 1_

```json
{
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
    "name" : "Foo 10",
    "email" : "foo10@bar.com",
    "category" : "office supplies",
    "description" : "iPad for office use",
    "link" : "http://www.apple.com/shop/buy-ipad/ipad-pro",
    "estimated_costs" : "800",
    "submit_date" : "12-10-2016"
}
```




### Abstract

In this assignment, you will be building another component for the assignment 1 expense management application to achieve the following:

* Dynamic Replica Registration
* Dynamic Load Balancing 
* Failure Detection


### Prerequistes

* Completed the assignment 1.

### Requirements

* Dynamic Replica Registration

A new component called Router will be implemented based on this tiny [Python TCP proxy server](http://voorloopnul.com/blog/a-python-proxy-in-less-than-100-lines-of-code/). 
First, make sure you understand the code and can proxy to two hosts (E.g. google.com and bing.com) in your local environment. 

As part of the node registration, whenever you launch the expense management application's Docker instance, it will auto-register to the own instance
to the router.


* Failure Detection (via CircutBreaker)

Whenever a node reaches its CircuitBreaker's error count, the router should deregister the failed node from the routing table in Redis and forward the same request to the next available node.  
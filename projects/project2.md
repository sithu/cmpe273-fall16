## 2. Trip Planner using Uber vs Lyft's Price Estimation

### Requirement

* Plan a trip which consists of a set of places and estimate the total cost between Uber and Lyft.
* You need to store location details and price estimate data into a persistent DB.
* FEEL FREE TO ADD ANY APIS THAT YOU NEED.

#### I. Location APIs

* 1. Create Location: POST /locations

> Call Google Map API to look up coordinates. http://maps.google.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=false

__Request__

```json
{
   "name" : "My Home",
   "address" : "123 Main St",
   "city" : "San Francisco",
   "state" : "CA",
   "zip" : "94113"
}
```

__Response__

```json
{
   "id" : 12345,
   "name" : "My Home",
   "address" : "123 Main St",
   "city" : "San Francisco",
   "state" : "CA",
   "zip" : "94113",
   "coordinate" : { 
      "lat" : 38.4220352,
      "lng" : -222.0841244
   }
}
```

* 2. Get a location: GET /locations/12345

__Response__

```json
{
   "id" : 12345,
   "name" : "My Home",
   "address" : "123 Main St",
   "city" : "San Francisco",
   "state" : "CA",
   "zip" : "94113",
   "coordinate" : { 
      "lat" : 38.4220352,
      "lng" : -222.0841244
   }
}
```

* 3. Update a location: PUT /locations/12345

__Request__

```json
{
   "name" : "My New Home"
}
```

* 4. Delete a location: DELETE /locations/12345

#### II. Trip Planner APIs

* 1. Plan a trip: POST /trips

__Request__

```json
{
    "start": "/locations/12345",
    "others" : [ 
        "/locations/1000",
        "/locations/1001",
        "/locations/1002",
    ],
    "end": "/locations/12345"
}
```

__Response__

```json
{
    "id": 200000,
    "start": "/locations/12345",
    "best_route_by_costs" : [ 
        "/locations/1002",
        "/locations/1000",
        "/locations/1001",
    ],
    "providers" : [
        {
            "name" : "Uber",
            "total_costs_by_cheapest_car_type" : 125,
            "currency_code": "USD",
            "total_duration" : 640,
            "duration_unit": "minute",
            "total_distance" : 25.05,
            "distance_unit": "mile"
        },
        {
            "name" : "Lyft",
            "total_costs_by_cheapest_car_type" : 110,
            "currency_code": "USD",
            "total_duration" : 620,
            "duration_unit": "minute",
            "total_distance" : 25.05,
            "distance_unit": "mile"
        }
    ],
    "end": "/locations/12345"
}
```

### Dependency

- [Lyft Pricing API](https://developer.lyft.com/docs/availability-cost)
- [Uber Pricing API](https://developer.uber.com/docs/ride-requests/references/api/v1-estimates-price-get)

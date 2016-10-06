### Requirements

You will be building a simple RPC application to check crime report for a location. You will be using (Spyne)[http://spyne.io/#inprot=HttpRpc&outprot=JsonDocument&s=rpc&tpt=WsgiApplication&validator=true] 
toolkit to build the application. Input protocol is HttpRpc and output is JSON as described below.

#### Input (HttpRpc)

* lat - latitude of a location
* lon - longitude of a location
* radius - radius distance in miles.


```sh
curl "http://localhost:8000/checkcrime?lat=37.334164&lon=-121.884301&radius=0.02"
```

#### Output (Json)

```json
{
    "total_crime" : 24,
    "crime_type_count" : {
        "Assault" : 10,
        "Arrest" : 8,
        "Burglary" : 6,
        "Robbery" : 4,
        "Theft" : 2,
        "Other" : 1
    },
    "event_time_count" : {
        "12:01am-3am" : 5,
        "3:01am-6am" : 0,
        "6:01am-9am" : 1,
        "9:01am-12noon" : 2,
        "12:01pm-3pm" : 2,
        "3:01pm-6pm" : 1,
        "6:01pm-9pm" : 0,
        "9:01pm-12midnight" : 9
    } 
}
```

### Dependency

#### CrimeReport API

```sh
# Example Crime Report near SJSU
curl -i "https://api.spotcrime.com/crimes.json?lat=37.334164&lon=-121.884301&radius=0.02&key=."
```
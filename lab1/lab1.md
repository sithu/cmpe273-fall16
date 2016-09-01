#### Purpose

#### Pre-requisite
* Github Account


#### Steps

1. [Install Docker]
2. Create a Github repo called "cmpe273-lab1" and clone the repo to your local machine.
```sh
git clone https://github.com/{your_username}/cmpe273-lab1
cd cmpe273-lab1
```
3. Create *requirements.txt* file and add this line to the file.
```sh
flask
```

4. Create a Python script *app.py* file and add these code to the file.
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
```


5. Create a Docker file *Dockerfile* without any file extension and add these lines to the file.
```sh
FROM python:3.5.2
MAINTAINER Your Name "yourname@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
```

6. Run this command inside the cmpe273-lab1 working directory. Make sure you have all these files in the current directory: Dockerfile, app.py, and requirements.txt
```sh
docker build -t lab1-flask-app:latest .
```

7. Run this Docker command to list all images.
```sh
docker images
```

8. Run the Docker container using the image you created in the previous step.
```sh
docker run -d -p 5000:5000 lab1-flask-app
```

9. Lookup IP of the Lab1-flask-app container.
```sh
docker-machine ls
```
```sh
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER    ERRORS
default   *        virtualbox   Running   tcp://192.168.99.100:2376           v1.11.1   
tester    -        virtualbox   Saved                                         Unknown   
```
> Example: Under the "URL" column, "192.168.99.100" is the IP of your container.

10. Open this URL in a web browser and you will see the Hello message. 

```sh
http://{IP_FROM_STEP_9}/
```

[Docker Cheat Sheet](https://github.com/wsargent/docker-cheat-sheet)

[Install Docker]: https://docs.docker.com/engine/installation/#/on-osx-and-windows{:target="_blank"}

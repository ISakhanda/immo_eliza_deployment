# immo_eliza_deployment

## DESCRIPTION
API that can handle a machine learning model in Python.
Project with a  ML model that can predict the price of a house and an apartament in Belgium. 
This python module contain all the code to preprocess the data.


My app.py file create an API that contains:

- A route at / that accept:
  GET request and return "alive" if the server is alive.

- A route at /predict that accept:
  POST request that receives the data of a house in JSON format.
  GET request returning a string to explain what the POST expect (data and format).


## INSTALLATION 
You can use a Dockerfile that allow you to build images for Docker.
run the Dockerfile:" $ docker run -it -p 8000:8000 your_image "

You can see all you need to install in the reauirements.txt


## USAGE
This can be deployed on any web server for predict the the price of a house and an apartament in Belgium. 

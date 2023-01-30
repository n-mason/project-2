# UOCIS322 - Project 2 #

## Name: Nathaniel Mason

## Contact Info: nmason@uoregon.edu

## Brief Project Description: 
This project's goal is to implement some logic that will determine if a file exists in the "pages/" directory. Along with this logic, some code was added in app.py to allow the application to parse "credentials.ini" or, if "credentials.ini" could not be found, to parse "default.ini". Parsing these ini files allows the program to determine the debug mode and the port to use. The user can edit these values in their "credentials.ini" file if they choose to. Note: "credentials.ini" should be placed in the web/ directory for app.py to function correctly.

### Testing:
To start the server, use the following docker commands:
* Use "docker build -t your_image_name ." to build the image, replacing your_image_name with your desired image name
* Next, use "docker run -d -p 5001:5000 your_image_name" to forward your docker container's port 5000 to your local port 5001 (the port 5001 will be the port you access on your browser). The port number does not need to be 5001, you can change this if you wish (docker container should use port 5000 though).
* Now, the docker image has been built and the docker container is running, so you can test it on your browser! You can also use "docker ps" to view the running docker container

Once the server is started, to test if a file exists you can use your browser to access the address at the port you specified. For example, localhost:5001/test.html. Curl could be used to test a request as well. 

* If the file specified in the request exists, a 200 OK header will be transmitted and then the content of the file will be displayed.
* If the file specified in the request does not exist, a 404 Not Found error code will be transmitted in the header and then a small informational message will be displayed.
* If the request contains ".." or "~", a 403 Forbidden error code will be transmitted in the header and then a small informational message will be displayed letting the user know that these characters are not allowed in the requests. 

To remove the container and image, use the following commands:
* "docker stop CONTAINER_ID", replace CONTAINER_ID with your container id that gets listed when entering docker ps
* "docker rm CONTAINER_ID", doing the same replacement you just did in the previous step
* "docker image rm your_image_name" to remove the image that was built
* At this point, using the command "docker images" should not list the image that was built earlier

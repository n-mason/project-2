# UOCIS322 - Project 2 #

## Name: Nathaniel Mason

## Contact Info: nmason@uoregon.edu

## Brief Project Description: 
This is the start of a project description...

### Testing:
Once the server is started, to test if a file exists you can use your browser to access the address at the port you specified (for example, localhost:5001/test.html). Curl could be used to test a request as well. 

* If the file specified in the request exists, a 200 OK header will be transmitted and then the content of the file will be displayed.
* If the file specified in the request does not exist, a 404 Not Found error code will be transmitted in the header and then a small informational message will be displayed.
* If the request contains ".." or "~", a 403 Forbidden error code will be transmitted in the header and then a small informational message will be displayed letting the user know that these characters are not allowed in the requests. 

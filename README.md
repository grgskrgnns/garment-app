# Garments App

The application was developped with the aim to complete the following task:

to build a (single page) website that I can search for a garment (e.g. black hat) and
it should display the garments that match the search criteria.

- Design an infrastructure architecture diagram that can be used to scale the website to
thousands of searches per second
Submission Requirements:


## General Design

The technologies used are ReactJS for the frontend and Python for the backend.
The website should load garments from a MongoDB database. The database is an Atlas Mongodb loaded with data from a given file.

### Architecture

The user is provided with access to the search page when logged in. A Django user access is implemented and JWT authentication is used between frontend and backend.
For test purposes a user account with access privileges has been created.
The backend then provides access to the search page and queries the Atlas MongoDB database.
For efficiency the search is executed when 3 characters are given.


### Scaling`

The decoupled design provides the capability to scale accordingly. Not all requests are served by the same server. 
The deployment is implemented with docker containers giving the capability for load balance and scaling 
by the use of appropriate tools.Queries are send to the database concerning the code of the item and the description. 




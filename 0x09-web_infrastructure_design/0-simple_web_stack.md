SIMPLE WEB STACK

DESCRIPTION:
This web infrastructure is designed to host a website accessible via www.foobar.com. It utilizes a single server, incorporating key components such as a web server (Nginx), an application server, a database (MySQL), and the necessary domain configuration. The server handles user requests, translating the domain name into an IP address, and efficiently processing web traffic.


>User's Intent:

A user expresses the intent to access the website by typing "www.foobar.com" into their web browser.


>The Domain Name System (DNS) translates the human-readable domain "www.foobar.com" into a server IP address (e.g., 8.8.8.8).


What is a Server:

A server is a physical or virtual machine capable of hosting and serving web content.
It receives, processes, and responds to user requests, facilitating the functioning of web applications.

What is the role of the Domain Name:

The domain name (www.foobar.com) acts as a human-readable alias for the server's IP address.
It provides an easy-to-remember way for users to access the website.

What type of DNS Record for www.foobar.com:

The DNS record type for www.foobar.com is a CNAME (Canonical Name) record.
This CNAME record points to the canonical name of the domain, which, in this case, is the domain itself.

Role of the Web Server (Nginx):

Nginx serves as the web server, handling incoming HTTP requests.
It acts as a reverse proxy, directing traffic and managing static content efficiently.

Role of the Application Server:

The application server (e.g., uWSGI) executes server-side code, handling dynamic content requests.
It communicates with the web server to process dynamic requests generated from the application codebase.

Role of the Database (MySQL):

MySQL serves as the relational database management system (RDBMS).
It stores and retrieves data for the web application, interacting with the application server.

Server Communication with User's Computer:

The server communicates with the user's computer using the HTTP/HTTPS protocol.
The web server responds to user requests, transmitting web pages and content to the user's browser.


Issues with the Infrastructure:
1.Single Point of Failure (SPOF):

The entire infrastructure relies on a single server, which can be a point of failure.
If the server goes down, the entire website becomes inaccessible.


2.Downtime during Maintenance:

Deploying new code or performing maintenance requires restarting the web server.
During this restart, the website may experience downtime.

3.Scalability Concerns:

The infrastructure may struggle to handle a large influx of incoming traffic.
Scaling options, such as load balancing and multiple servers, are not implemented, limiting scalability.

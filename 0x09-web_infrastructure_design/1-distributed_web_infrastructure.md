Two-Server Web Infrastructure for www.foobar.com

Description:
This enhanced web infrastructure incorporates two servers for increased reliability and scalability. It features a load balancer (HAproxy) to distribute incoming traffic, ensuring efficient utilization of resources. Additionally, a Primary-Replica (Master-Slave) database cluster with MySQL is implemented to enhance data availability and redundancy.

User Access:

User's Intent:

A user intends to access the website by typing "www.foobar.com" into their web browser.
Domain Name (DNS):

The Domain Name System (DNS) translates the human-readable domain "www.foobar.com" into the load balancer's IP address.


Load Balancer:

A load balancer (HAproxy) evenly distributes incoming traffic between two servers.
It enhances reliability by ensuring that neither server is overloaded, contributing to optimal performance.


Servers (Server 1 and Server 2):

Two servers (Server 1 and Server 2) host the web infrastructure, enabling load distribution and redundancy.
Each server contains a copy of the application files and is equipped to handle user requests.


Web Server (Nginx):

Nginx serves as the web server, managing incoming HTTP requests and handling static content efficiently.
It is installed on both Server 1 and Server 2 for redundancy and load balancing.


Application Server:

The application server (e.g., Gunicorn) executes server-side code, handling dynamic content requests.
It communicates with the web server and is present on both Server 1 and Server 2 for redundancy.


Database (MySQL) Cluster:

The MySQL database is configured as a Primary-Replica (Master-Slave) cluster for data redundancy and availability.
The Primary node handles write operations, while the Replica node(s) handle read operations.


Specifics about the Infrastructure:
Why Add Additional Servers:

Increased redundancy and fault tolerance by distributing load between two servers.
Enhanced scalability to handle a larger number of simultaneous user requests.

Why Add a Load Balancer:

To distribute incoming traffic evenly, preventing overload on a single server.
Improved reliability and availability by ensuring continuous service even if one server fails.

Load Balancer Distribution Algorithm:

The load balancer uses a Round Robin distribution algorithm.
Each incoming request is directed to the next server in line, distributing the load evenly.

Load Balancer Setup: Active-Active vs. Active-Passive:

The setup is Active-Active.
Both servers actively handle user requests, providing redundancy and load distribution.
Active-Passive would involve one server handling requests while the other is on standby.

Primary-Replica Database Cluster:

The Primary-Replica cluster ensures data redundancy and availability.
Write operations are handled by the Primary node, while Replica node(s) handle read operations.
Difference Between Primary and Replica Nodes:

The Primary node processes write operations and is the authoritative source for data changes.
Replica nodes replicate data from the Primary and handle read operations, providing fault tolerance.



Infrastructure Issues:

Single Point of Failure (SPOF):

The load balancer is a potential single point of failure.
Security issues due to the absence of a firewall and lack of HTTPS encryption.
Monitoring is not implemented, leading to potential challenges in identifying and resolving issues promptly.

Security Issues:

Lack of a firewall exposes the infrastructure to potential security threats.
Absence of HTTPS encryption poses a risk of data interception during transmission.


No Monitoring:

The absence of monitoring tools limits the ability to identify and address performance issues proactively.

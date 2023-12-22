Secured, Encrypted, and Monitored Three-Server Web Infrastructure for www.foobar.com



Description:
This design focuses on enhancing security, encryption, and monitoring in a three-server web infrastructure. It incorporates firewalls for added security, SSL certificates to serve encrypted traffic over HTTPS, and monitoring clients to ensure proactive monitoring and issue resolution.

User Access:
User's Intent:

A user intends to access the website by typing "www.foobar.com" into their web browser.

Domain Name (DNS):

The Domain Name System (DNS) translates the human-readable domain "www.foobar.com" into the load balancer's IP address.

Load Balancer:

A load balancer (Nginx) evenly distributes incoming traffic between three servers for load distribution and redundancy.
It is configured to terminate SSL at the load balancer level.

Servers (Server 1, Server 2, and Server 3):

Three servers host the web infrastructure, providing redundancy and load distribution.
Each server contains components for the database, web server, and application server.

Firewalls:

Firewalls are implemented to control incoming and outgoing network traffic.
They add an additional layer of security by filtering and monitoring traffic based on predetermined security rules.

Web Server (Nginx):

Nginx serves as the web server, managing incoming HTTP requests and handling static content efficiently.
It is configured to terminate SSL connections, providing secure communication between the user and the load balancer.

SSL Certificate:

An SSL certificate is used to enable HTTPS, securing the communication between the user's browser and the web infrastructure.
It ensures that data transmitted between the user and the website remains encrypted and secure.

Application Server:

The application server (e.g., Gunicorn) executes server-side code, handling dynamic content requests.
It communicates with the web server and processes user requests.

Database (MySQL) Cluster:

The MySQL database is configured as a Primary-Replica (Master-Slave) cluster for data redundancy and availability.
The Primary node handles write operations, while Replica nodes handle read operations.

Monitoring Clients:

Monitoring clients (e.g., Sumologic) collect and send data to a centralized monitoring service.
They are configured to collect metrics, logs, and other relevant data for performance analysis and issue detection.
Specifics about the Infrastructure:

Why Add Additional Firewalls:

Firewalls provide an additional layer of security, controlling and monitoring incoming and outgoing traffic.
They help prevent unauthorized access and protect against potential security threats.

Why Terminate SSL at the Load Balancer Level:

Terminating SSL at the load balancer level simplifies SSL certificate management.
It offloads the SSL decryption process from backend servers, improving efficiency and performance.

Why Serve Traffic Over HTTPS:

HTTPS encrypts the communication between the user's browser and the web infrastructure.
It ensures data confidentiality, integrity, and authenticity, protecting sensitive information.

Why Use Monitoring:

Monitoring is crucial for proactive issue detection, performance analysis, and infrastructure optimization.
It helps identify and address potential problems before they impact user experience.

How Monitoring Tools Collect Data:

Monitoring clients collect data such as server metrics, logs, and performance indicators.
Data is sent to a centralized monitoring service (e.g., Sumologic) for analysis and visualization.

Monitoring Web Server QPS:

To monitor web server QPS (Queries Per Second), configure monitoring tools to track server metrics related to request rates.
Set up alerts to notify administrators if QPS exceeds predefined thresholds.
Infrastructure Issues:

Terminating SSL at the Load Balancer Level:

While simplifying SSL management, terminating SSL at the load balancer level exposes decrypted traffic between the load balancer and backend servers.

Single MySQL Server Accepting Writes:

A single MySQL server accepting writes introduces a Single Point of Failure (SPOF).
It can lead to data inconsistencies and potential downtime if the primary server fails.

Uniform Components Across Servers:

Having servers with identical components may lead to uniform vulnerabilities.
If a common vulnerability affects one server, it may impact all servers simultaneously.

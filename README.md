# Microservices Load Balancer
This project implements a microservices load balancer using Flask, designed to handle dynamic configuration updates, support multiple load balancing algorithms, provide HTTPS to microservices, implement circuit breakers and retries, offer a clean web UI, and support WebSocket and HTTP/2 protocols.

## Features
1. Load Balancing Algorithms:
Implements Round Robin, Least Connections, and Weighted Round Robin algorithms.

2. Dynamic Configuration:
Dynamically updates configuration without requiring restarts.

3. Health Checks:
Implements health checks to direct traffic only to healthy servers.

4. Scalability:
Designed to scale horizontally, supporting auto-discovery of new servers and dynamic configuration updates.

5. Logging and Monitoring:
Provides logging to track requests, responses, and server health.
Integrates with monitoring tools for performance insights.

6. Security:
Ensures secure handling of traffic, supporting SSL termination and security protocols.

7. Circuit Breakers and Retries:
Implements circuit breakers and retry mechanisms for enhanced reliability.
WebSocket and HTTP/2 Support:

8. Supports WebSocket and HTTP/2 protocols for diverse microservices communication.

## Getting Started
- Installation:
`pip install Flask`
- Run the Flask App:
`python app.py`
- Configuration:
Update configuration dynamically using the /update-config endpoint.
- Web UI:
Access the web UI at `http://localhost:5000`.

## Usage
- Processing Requests:
Send requests to the load balancer endpoint (/) for load-balanced processing.
- Health Checks:
Check the health of the load balancer at /health.
- Updating Configuration:
Use the /update-config endpoint to dynamically add or remove servers.

## Contributing
Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a pull request.


## License
This project is licensed under the MIT License.


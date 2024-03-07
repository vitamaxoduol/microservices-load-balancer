import logging
from prometheus_client import start_http_server, Counter

class LoggingMonitoring:
    
    def __init__(self, port: int = 8000) -> None:

        """
        Initialize LoggingMonitoring with basic logging and Prometheus metrics setup.
        Args:
            port (int): The port for the Prometheus HTTP server. Default is 8000.
        """
        logging.basicConfig(filename='app.log', level=logging.INFO)
    
        # Prometheus metrics setup
        start_http_server(port)
        self.request_counter = Counter('requests_total', 'Total number of requests')


    def log_request(self, server: str) -> None:
        '''
            Log the routing of a request  to a specific server
            Args:
            server (str): The server to which the request is routed.
        '''
        logging.info(f"Request routed to {server}")
        self.request_counter.inc()

    def log_health_check(self, status: str) -> None:
        '''
            Log the result of a health check
            Args:
            status (str): The status of the health check.
        '''
        logging.info(f"Health check status: {status}")


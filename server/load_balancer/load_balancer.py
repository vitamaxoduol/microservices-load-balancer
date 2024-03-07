from load_balancer.algorithms import RoundRobinAlgorithm
from logging_monitoring.logging_monitoring import LoggingMonitoring

class LoadBalancer:
    def __init__(self) -> None:
        self.servers = ['http://server1', 'http://server2', 'http://server3', 'http://server4']
        self.algorithm = RoundRobinAlgorithm(self.servers)


    def process_request(self):
        """
            Process a request  by forwarding it to the next available server
        """
        next_server = self.algorithm.get_next_server()

        # Log the routing of the request
        LoggingMonitoring.log_request(next_server)

        response = f'Request processed by: {next_server}'     
        return {'message': response}
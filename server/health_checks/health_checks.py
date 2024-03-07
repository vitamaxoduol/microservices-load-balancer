import requests


class HealthChecks:
    def __init__(self, load_balancer) -> None:
        self.load_balancer = load_balancer


    def check_health(self):
        """
            Check the health for the load balancer.
        """
        is_healthy = self.is_load_balancer_healthy()
        return{'status': 'Okay' if is_healthy else 'Unhealthy'}
    
    def is_load_balancer_healthy(self):
        """
          Check the health of the load balancer by 
          sending a simple HTTP request to each server.  
        """

        for server in self.load_balancer.servers:
            try:
                response = requests.get(server, timeout=2)

                if response.status_code // 100==2:
                    return True
            except requests.RequestException:
                return False
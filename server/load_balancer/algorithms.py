class RoundRobinAlgorithm:
    def __init__(self, servers) -> None:
        self.servers = servers
        self.current_index = 0

    def get_next_serber(self):
        """
            Get the next server in the roound-robin fashion
        """

        server = self.servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.servers) 
        return server
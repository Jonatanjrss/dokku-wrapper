from .services.apps import Apps
from .services.domains import Domains
from .services.config import Config


class Dokku:
    """Interface principal para interação com o Dokku."""

    def __init__(self):
        self.apps = Apps()
        self.domains = Domains()
        self.config = Config()

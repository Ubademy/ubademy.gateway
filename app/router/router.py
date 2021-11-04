import logging

from app.router.router_exception import InvalidMicroserviceError
from app.service_caller.service_caller import ServiceCaller

logger = logging.getLogger(__name__)


class Router:
    def __init__(self, microservices: dict):
        self.microservices = microservices

    def get_service_caller(self, path: str) -> ServiceCaller:
        service_name = path.split("/")[0]
        logger.info(service_name)
        if not self.__is_microservice(service_name):
            raise InvalidMicroserviceError

        return ServiceCaller(
            service_url=self.microservices.get(service_name),
            path=path,
        )

    def __is_microservice(self, name: str):
        return name in self.microservices

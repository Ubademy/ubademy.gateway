import logging

from app.caller.caller import Caller
from app.caller.multi_service_caller import MultiServiceCaller
from app.caller.service_caller import ServiceCaller
from app.router.router_exception import InvalidMicroserviceError

logger = logging.getLogger(__name__)


class Router:
    def __init__(self, microservices: dict):
        self.microservices = microservices

    def get_service_caller(self, path: str) -> Caller:
        service_name = path.split("/")[0]
        logger.info(service_name)
        if self.__is_special_service(service_name):
            logger.info("Special service")
            return MultiServiceCaller(
                count=len(service_name.split(".")),
                router=self,
            )

        if not self.__is_microservice(service_name):
            raise InvalidMicroserviceError

        return ServiceCaller(
            service_url=self.microservices.get(service_name),
            path=path,
        )

    def __is_microservice(self, name: str):
        return name in self.microservices

    def __is_special_service(self, service_name):
        services = service_name.split(".")
        return (
            len(services) == 2
            and self.__is_microservice(services[0])
            and self.__is_microservice(services[1])
        )

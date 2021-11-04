import logging

from app.parser.parser_exception import InvalidMicroserviceError
from app.service_caller.service_caller import ServiceCaller

logger = logging.getLogger(__name__)

microservices = {
    "users": "https://ubademy-service-users.herokuapp.com/",
    "courses": "https://ubademy-service-courses.herokuapp.com/",
}


class Parser:
    @classmethod
    def get_service_caller(cls, path: str) -> ServiceCaller:
        service_name = path.split("/")[0]
        logger.info(service_name)
        if not Parser.is_microservice(service_name):
            raise InvalidMicroserviceError

        return ServiceCaller(
            service_url=microservices.get(service_name),
            path=path,
        )

    @classmethod
    def is_microservice(cls, name: str):
        return name in microservices

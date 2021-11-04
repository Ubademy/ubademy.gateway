import pytest

from app.router.router import Router
from app.router.router_exception import InvalidMicroserviceError


class TestRouter:
    def test_get_service_caller_should_throw_invalid_microservice_error(self):
        microservices = {"service_1": "service_1.com", "service_2": "service_1.com"}
        router = Router(microservices=microservices)
        with pytest.raises(InvalidMicroserviceError):
            router.get_service_caller("service_0/index")

    def test_get_service_caller_should_return_service_caller_with_correct_url(self):
        microservices = {"service_1": "service_1.com/", "service_2": "service_1.com/"}
        router = Router(microservices=microservices)

        assert (
            router.get_service_caller("service_1/index").url
            == "service_1.com/service_1/index"
        )

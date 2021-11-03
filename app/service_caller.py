from starlette.requests import Request


class ServiceCaller:
    def __init__(self, service_url: str):
        self.service_url = service_url

    def call_with_request(self, request: Request):
        raise NotImplementedError

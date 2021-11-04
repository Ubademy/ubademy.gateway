import logging

import requests
from starlette.requests import Request

logger = logging.getLogger(__name__)


class ServiceCaller:
    def __init__(
        self,
        service_url: str,
        path: str,
    ):
        self.headers = None
        self.body = None
        self.service_url = service_url
        self.path = path
        self.requests = {
            "GET": ServiceCaller.get,
            "POST": ServiceCaller.post,
            "PUT": ServiceCaller.put,
            "DELETE": ServiceCaller.delete,
        }

    async def call_with_request(self, request: Request):
        func = self.requests.get(request.method)
        # headers = {}
        # for i in request.headers.keys():
        #    headers[i] = request.headers.get(i)
        # if len(headers.keys()) == 0:
        #    headers = None
        data = await request.form()
        headers = None
        url = self.service_url + self.path

        return func(headers, url, data)

    @classmethod
    def get(cls, headers: dict, url: str, data: dict):
        logger.info(url)
        return requests.get(url, headers=headers, data=data)

    @classmethod
    def post(cls, headers: dict, url: str, data: dict):
        logger.info(url)
        return requests.post(url, headers=headers, data=data)

    @classmethod
    def put(cls, headers: dict, url: str, data: dict):
        logger.info(url)
        return requests.put(url, headers=headers, data=data)

    @classmethod
    def delete(cls, headers: dict, url: str, data: dict):
        logger.info(url)
        return requests.delete(url, headers=headers, data=data)

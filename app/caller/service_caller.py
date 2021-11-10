import logging
from typing import Optional

import requests
from requests import Session
from starlette.requests import Request

from app.caller.caller import Caller, get_headers_from_request, get_params_from_request

logger = logging.getLogger(__name__)


class ServiceCaller(Caller):
    def __init__(
        self,
        service_url: str,
        path: str,
        session: Optional[Session] = requests.Session(),
    ):
        self.headers = None
        self.data = None
        self.params = None
        self.session = session
        self.url = service_url + path
        self.requests = {
            "GET": self.get,
            "POST": self.post,
            "PUT": self.put,
            "DELETE": self.delete,
        }

    async def call_with_request(self, request: Request):
        logger.info(request.method)
        func = self.requests.get(request.method)
        logger.info(request.headers)
        self.headers = get_headers_from_request(request.headers)
        logger.info("done")
        logger.info(request.query_params)
        self.params = get_params_from_request(request.query_params)

        try:
            self.data = await request.json()
        except:
            self.data = None

        logger.info(self.data)
        return func()

    async def call_with_data(
        self, method: str, headers: dict, params: dict, data: dict
    ):
        func = self.requests.get(method)
        self.headers = headers
        self.params = params
        self.data = data

        return func()

    def get(self):
        return self.session.get(
            self.url, headers=self.headers, json=self.data, params=self.params
        )

    def post(self):
        return self.session.post(
            self.url, headers=self.headers, json=self.data, params=self.params
        )

    def put(self):
        return self.session.put(
            self.url, headers=self.headers, json=self.data, params=self.params
        )

    def delete(self):
        return self.session.delete(
            self.url, headers=self.headers, json=self.data, params=self.params
        )

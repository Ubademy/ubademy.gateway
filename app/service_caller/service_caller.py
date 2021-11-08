import logging
from typing import List, Optional

import requests
from requests import Session
from starlette.datastructures import Headers, QueryParams
from starlette.requests import Request

logger = logging.getLogger(__name__)

good_headers: List[str] = []


def get_headers_from_request(h: Headers) -> Optional[dict]:
    headers = {}
    for i in h.keys():
        if i in good_headers:
            headers[i] = h.get(i)
    if len(headers.keys()) == 0:
        headers = None

    return headers


def get_params_from_request(p: QueryParams):
    params = {}
    for i in p.keys():
        params[i] = p.get(i)
    if len(params.keys()) == 0:
        params = None

    return params


class ServiceCaller:
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
        func = self.requests.get(request.method)
        self.headers = get_headers_from_request(request.headers)
        self.params = get_params_from_request(request.query_params)
        try:
            self.data = await request.json()
        except:
            self.data = None

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

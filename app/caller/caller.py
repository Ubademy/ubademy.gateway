import json
import os
from typing import Optional

from starlette.datastructures import Headers, QueryParams
from starlette.requests import Request

try:
    good_headers = json.loads(os.environ["GOOD_HEADERS"])
except KeyError as e:
    good_headers = []


def get_headers_from_request(h: Headers) -> Optional[dict]:
    headers = {}
    for i in h.keys():
        if i in good_headers:
            headers[i] = h.get(i)
    if len(headers.keys()) == 0:
        headers = {}

    return headers


def get_params_from_request(p: QueryParams):
    params = {}
    for i in p.keys():
        params[i] = p.get(i)
    if len(params.keys()) == 0:
        params = {}

    return params


class Caller:
    async def call_with_request(self, request: Request):
        raise NotImplementedError

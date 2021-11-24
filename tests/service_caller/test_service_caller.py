from unittest.mock import MagicMock, Mock

import pytest

from app.caller.service_caller import ServiceCaller


def mocked_get(url, headers, json):
    if url == "service_1.com/service_1" and not headers and not json:
        return "done"
    return "error"


def mocked_post(url, headers, json):
    if url == "service_1.com/service_1" and not headers and not json:
        return "done"
    return "error"


async def mocked_async():
    return None


class TestServiceCaller:
    @pytest.mark.asyncio
    async def test_call_with_request_get_should_call_url(self):
        session = MagicMock()
        session.get = Mock(side_effect=mocked_get)
        request = MagicMock()
        request.method = "GET"
        request.json = Mock(side_effect=mocked_async)
        request.headers = {"header_1": "value_1"}
        request.query_params = {}

        caller = ServiceCaller(
            service_url="service_1.com/", path="service_1", session=session
        )
        response = await caller.call_with_request(request=request)
        assert response == "done"

    @pytest.mark.asyncio
    async def test_call_with_data_post_should_call_url(self):
        session = MagicMock()
        session.post = Mock(side_effect=mocked_post)

        caller = ServiceCaller(
            service_url="service_1.com/", path="service_1", session=session
        )
        response = await caller.call_with_data(
            method="POST", headers={}, params={}, data={}
        )
        assert response == "done"

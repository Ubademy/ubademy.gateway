from unittest.mock import MagicMock, Mock

import pytest

from app.caller.multi_service_caller import MultiServiceCaller


async def mocked_request():
    return {"methods": ["GET"], "paths": ["courses"], "params": [{}]}


async def mocked_response(method, headers, params, data):
    if method == "GET" and headers == {} and params == {} and data == {}:
        return "done"
    return "error"


class TestServiceCaller:
    @pytest.mark.asyncio
    async def test_call_with_request_get_should_call_url(self):
        service_caller = MagicMock()
        service_caller.call_with_data = Mock(side_effect=mocked_response)
        request = MagicMock()
        request.json = Mock(side_effect=mocked_request)
        request.headers = {}
        router = MagicMock()
        router.get_service_caller = Mock(return_value=service_caller)

        caller = MultiServiceCaller(count=1, router=router)
        response = await caller.call_with_request(request=request)
        assert response == "done"

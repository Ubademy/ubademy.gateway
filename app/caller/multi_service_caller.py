import logging

from starlette.requests import Request

from app.caller.caller import Caller, get_headers_from_request

logger = logging.getLogger(__name__)


def get_data(service_response):
    try:
        data = service_response.json()
    except:
        data = {}

    return data


class MultiServiceCaller(Caller):
    def __init__(self, count: int, router):
        self.count = count
        self.router = router

    async def call_with_request(self, request: Request):
        try:
            data = await request.json()
        except:
            raise
        logger.info("Called cross service")
        logger.info(data)
        service_response = {}
        for i in range(self.count):
            caller = self.router.get_service_caller(path=(data.get("paths")[i]))
            logger.info(caller)
            logger.info(data.get("methods")[i])
            logger.info(get_data(service_response))
            logger.info(get_headers_from_request(request.headers))
            logger.info(data.get("params")[i])
            service_response = await caller.call_with_data(
                method=data.get("methods")[i],
                headers=get_headers_from_request(request.headers),
                params=data.get("params")[i],
                data=get_data(service_response),
            )

        return service_response

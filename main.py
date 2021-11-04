import logging
from logging import config

from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from app.parser.parser import Parser
from app.parser.parser_exception import InvalidMicroserviceError

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(title="gateway")


@app.api_route(
    "/{full_path:path}",
    status_code=status.HTTP_200_OK,
    methods=["GET", "POST", "PUT", "DELETE"],
    tags=["gateway"],
)
async def catch_all(request: Request, response: Response, full_path: str):
    try:
        logger.info(full_path)
        caller = Parser.get_service_caller(path=full_path)
        logger.info(caller)
        service_response = await caller.call_with_request(request=request)
        logger.info(service_response.text)
        response.status_code = service_response.status_code

    except InvalidMicroserviceError as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )

    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return "done"

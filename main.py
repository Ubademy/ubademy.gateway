import logging
from logging import config

from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.requests import Request

from app.parser import Parser

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(title="gateway")


@app.api_route("/{full_path}", status_code=status.HTTP_200_OK, tags=["gateway"])
async def catch_all(request: Request, full_path: str):
    try:
        caller = Parser.get_service_caller(url=full_path)
        caller.call_with_request(request=request)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return None

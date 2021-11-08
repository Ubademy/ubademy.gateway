import ast
import logging
import os
from logging import config

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from app.router.router import Router
from app.router.router_exception import InvalidMicroserviceError

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(title="gateway")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


try:
    microservices = ast.literal_eval(os.environ["MICROSERVICES"])
except KeyError as e:
    microservices = {}


@app.api_route(
    "/{full_path:path}",
    status_code=status.HTTP_200_OK,
    methods=["GET", "POST", "PUT", "DELETE"],
    tags=["gateway"],
)
async def catch_all(request: Request, response: Response, full_path: str):
    try:
        logger.info(full_path)
        router = Router(microservices=microservices)
        caller = router.get_service_caller(path=full_path)
        service_response = await caller.call_with_request(request=request)
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

    return service_response.json()


@app.options(
    "/{full_path:path}",
    status_code=status.HTTP_200_OK,
    tags=["gateway"],
)
async def options(full_path: str):
    logger.info(full_path)
    return "options"

import logging
from logging import config

from fastapi import FastAPI
from starlette.requests import Request

config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="gateway"
)


@app.route("/{full_path:path}")
async def catch_all(request: Request, full_path: str):

    return None

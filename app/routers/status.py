from app.fileutils import json_content
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..settings import SEASONS, VALHEIM_SERVER

router = APIRouter()


@router.get('/status')
async def status(s: str | None = None) -> JSONResponse:
    return JSONResponse(
        content=json_content(
            f'{VALHEIM_SERVER}/{s or SEASONS[0]}/data/htdocs/status.json',
        )
    )

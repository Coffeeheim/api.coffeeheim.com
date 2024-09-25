from http import HTTPStatus

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post('/permittedlist')
async def permittedlist() -> JSONResponse:
    return JSONResponse(
        content=None,
        status_code=HTTPStatus.CREATED,
    )

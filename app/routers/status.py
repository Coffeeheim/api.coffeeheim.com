from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get('/status')
async def status(s: str | None = None) -> JSONResponse:
    return JSONResponse(content={})

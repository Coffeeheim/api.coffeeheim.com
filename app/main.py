from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .configs import ALLOW_ORIGINS
from .routers import permittedlist, status

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(permittedlist.router)
app.include_router(status.router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

origins = [
    'https://coffeeheim.com',
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get('/status')
async def status():
    return JSONResponse({})


@app.post('/permittedlist')
async def permittedlist():
    return JSONResponse({})

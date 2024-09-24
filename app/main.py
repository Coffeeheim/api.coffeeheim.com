from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/status')
async def status():
    return JSONResponse({})


@app.post('/permittedlist')
async def permittedlist():
    return JSONResponse({})

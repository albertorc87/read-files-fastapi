import os
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/files/{file}")
async def get_file(file: str):
    if not os.path.isfile(f'./files/{file}'):
        raise HTTPException(status_code=404, detail='File not found')

    return FileResponse(f'./files/{file}')
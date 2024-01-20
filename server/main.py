import os
import shutil
from fastapi import FastAPI
from fastapi import UploadFile
from pathlib import Path

app = FastAPI()
SAVE_FILEPATH = "/tmp/simple-fileserver/"
Path(SAVE_FILEPATH).mkdir(parents=True, exist_ok=True)


@app.get("/")
def index():
    return "hello"


@app.post("/files/")
def upload_file(file: UploadFile):
    full_path = os.path.join(SAVE_FILEPATH, file.filename)
    try:
        with open(full_path, "wb") as destination:
            shutil.copyfileobj(file.file, destination)
    finally:
        file.file.close()
        print(f'Copying {full_path}')
    return {"filename": file.filename}

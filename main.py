import os.path
import shutil

from fastapi import FastAPI
from fastapi import UploadFile

app = FastAPI()
SAVE_FILEPATH = "/tmp/simple-fileserver/"


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
    return {"filename": file.filename}

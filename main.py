from fastapi import FastAPI, File, UploadFile
import os

app = FastAPI()
UPLOAD_DIR = "./uploads"

@app.post("/upload")
async def upload_file(video: UploadFile = File(...)):
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    file_path = os.path.join(UPLOAD_DIR, video.filename)
    with open(file_path, "wb") as f:
        f.write(await video.read())
    return {"filename": video.filename}

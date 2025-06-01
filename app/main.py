from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.model import is_cat_image
from io import BytesIO
from PIL import Image
from pathlib import Path

base_dir = Path(__file__).resolve().parent
static_dir = base_dir / "static"
template_dir = base_dir / "templates"

app = FastAPI()

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=template_dir)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/predict", response_class=HTMLResponse)
def predict(request: Request, file: UploadFile = File(...)):
    image_bytes = BytesIO(file.file.read())
    image = Image.open(image_bytes)
    result = is_cat_image(image)
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

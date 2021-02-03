from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/Login/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request, "id": id})


@app.get("/Login/?id", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("Login_result.html", {"request": request, "id": id})
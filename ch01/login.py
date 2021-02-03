import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from user import user_info

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse)
async def page(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})


@app.get("/Login/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})


@app.get("/Login/auth", response_class=HTMLResponse)
async def login_auth(request: Request, id: str, password: str):
    user_id = id
    user_pw = password
    if(user_info(user_id, user_pw)):
        return templates.TemplateResponse("login_result.html", {"request" : request, "id" : id})
    else :
        return templates.TemplateResponse("login.html", {"request" : request, "id" : id})

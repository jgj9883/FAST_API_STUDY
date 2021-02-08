import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from user import user_info

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# @app.get('/', response_class=HTMLResponse)
# async def page(request: Request):
#     return templates.TemplateResponse("Login.html", {"request": request})
#
#
# @app.get("/Login/", response_class=HTMLResponse)
# async def login(request: Request):
#     return templates.TemplateResponse("Login.html", {"request": request})
#

@app.get("/post", response_class=HTMLResponse)
async def post_test(request:Request):
    id = ""
    pwd = ""
    return templates.TemplateResponse("post.html", {"request":request, "id":id, "pwd":pwd})

@app.post("/post")
async def post_test(request:Request, id: str = Form(...), pwd:str = Form(...)):
    return id + pwd
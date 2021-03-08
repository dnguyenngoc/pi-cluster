from fastapi import FastAPI, Form, File, UploadFile, Body, Cookie
from fastapi.routing import APIRoute
from db.session import Session
from settings import config
from starlette.requests import Request
from typing import Callable, List, Optional
# from api.v1 import test
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
from starlette.responses import RedirectResponse
import datetime



app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json", docs_url="/api/docs")

# Mount static template
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")

# Router config
# app.include_router(test.route, prefix="/api/v1/test", tags=["Test"])

def generate_html_response(status, content):
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Status: {status}</h1>
            <h1>Content: {content}</h1>

        </body>
    </html>
    """.format(status = status, content = content)
    return HTMLResponse(content=html_content, status_code=status)


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse('login.html', context={'request': request})


@app.post("/login")
async def post_login(request: Request, username: str = Form(...), password: str= Form(...)):
    if username != 'admin' and password != '1q2w3e4r':
        return generate_html_response(400, "bad request!")
    else:
        rr = RedirectResponse('/', status_code=303)
        rr.set_cookie(key="token", value='yes')
        rr.set_cookie(key="expire", value= datetime.datetime.now() + datetime.timedelta(minutes=30))
        return rr
    

@app.get("/")
async def get_home(request: Request, token: Optional[str] = Cookie(None), expire: datetime = Cookie(None):
    if token == 'yes':
        if  expire < datetime.datetime.now():
            return templates.TemplateResponse('go-to-login.html', context={'request': request})
        else:
            return templates.TemplateResponse('main.html', context={'request': request})
    else:
        return templates.TemplateResponse('go-to-login.html', context={'request': request})


@app.post("/upload-file")
async def upload(file: UploadFile = File(...)):
    file_name = file.filename
    file_type = file.content_type
    value = file.file.read()
    with open(os.getcwd() + '/storage/' + file_name, 'wb+') as f:
        f.write(value)
    return {'file_name': file_name, 'file_type': file_type}


origins = ["http://localhost","http://localhost:4200",]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB config
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response

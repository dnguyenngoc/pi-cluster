from fastapi import Body
from fastapi import Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session

route = APIRouter()


@route.get("/hello1")
def hello1():
    return "hello1 world"


@route.get("/hello2")
def hello2():
    return "hello2 world"


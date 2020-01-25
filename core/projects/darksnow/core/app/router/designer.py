from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel
from typing import TypeVar, List
from ..db import dbinit
from ..service import designer

router = APIRouter()


class Designer(BaseModel):
    designer_id: str
    first_name: str
    last_name: str
    password: str


@router.get("/designer")
def read_root():
    # dbinit.init()
    return {"Hello": "World"}


@router.post("/user_login")
def login(designer_id: str, password: str):
    return designer.login(designer_id, password)


@router.get("/designer/{designer_id}")
def read_item(designer_id: str, q: str = None):
    return dbinit.get_designer(designer_id)
    # return {"item_id": designer_id, "q": q}


T = TypeVar("T")


@router.post("/designer/")
def create_designer(designer_object: Designer):
    designer.create_designer(designer_object.first_name, designer_object.last_name, designer_object.designer_id,
                             designer_object.password)
    if designer.get_designer(designer_object.designer_id) is not None:
        return 'user created successfully with name : ' + designer.get_designer(
            designer_object.designer_id).first_name + ' ' + designer.get_designer(designer_object.designer_id).last_name
    else:
        return 'user not created'


@router.post("/uploadfiles")
async def create_upload_files(designer_id: str, file: UploadFile = File(...)):
    return designer.upload_files(designer_id, file)


@router.get("/getfiles")
def get_files(designer_id: str):
    return designer.get_files(designer_id)


@router.get("/recent_data")
def recent_data(designer_id: str):
    return designer.recent_data(designer_id)

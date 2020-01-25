from typing import List

from fastapi import UploadFile, File

from ..db import designer
from .encryption import *
import boto3


def login(designer_id: str, password: str):
    session = boto3.session.Session()
    designer_obj = designer.login(designer_id)
    if designer != 'Designer does not exist':
        decrypt_password = decrypt(session, designer_obj.password)
        if decrypt_password == password:
            return 'login successful'
        else:
            return 'login unsuccessful'

    else:
        return designer


def create_designer(first_name: str, last_name: str, designer_id: str, password: str):
    session = boto3.session.Session()
    password = encrypt(session, password, 'alias/darksnow')
    designer.create_designer(first_name, last_name, designer_id, password)


def get_designer(designer_id: str):
    return designer.get_designer(designer_id)


def upload_files(designer_id: str, files: UploadFile = File(...)):
    return designer.upload_files(designer_id, files)


def get_files(designer_id: str):
    return designer.get_files(designer_id)


def recent_data(designer_id: str):
    return designer.recent_data(designer_id)
import json
import logging
import requests
from datetime import datetime

import boto3
from botocore.exceptions import ClientError
from fastapi import UploadFile, File
from ..model.dbmodel import DesignerModel, DesignerImageMap


def create_designer(first_name: str, last_name: str, designer_id: str, password: str):
    designer = DesignerModel(designer_id)
    designer.timestamp = datetime.now().timestamp()
    designer.first_name = first_name
    designer.last_name = last_name
    designer.password = json.dumps(password)
    designer.data = []
    designer.save()


def get_designer(designer_id: str):
    for designer in DesignerModel.query(designer_id):
        return designer


def login(designer_id: str):
    try:
        user = DesignerModel.get(designer_id)
        return user
    except DesignerModel.DoesNotExist:
        return 'Designer does not exist'


def get_files(designer_id):
    designer = get_designer(designer_id)
    for data in designer.data:
        image_url = create_presigned_url('darksnow', designer_id + '/' + data.image_name)
        data.image_url = image_url
    return designer.data


def create_presigned_url(bucket_name: str, object_name: str, expiration=30):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url(ClientMethod='get_object',
                                                    Params={
                                                        'Bucket': bucket_name,
                                                        'Key': object_name},

                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None
    return response


def upload_files(designer_id: str, files: UploadFile = File(...)):
    designer = get_designer(designer_id)
    # for file in files:
    #     current = datetime.now()
    #     image_info = DesignerImageMap(
    #         timestamp=current,
    #         image_url=file.filename,
    #         image_name=file.filename
    #
    #     )
    # files.filename = files.file.read()
    f = open(files.filename, "wb")
    f.write(files.file.read())
    f.close()
    image_url = 'https://' + 'darksnow' + '.s3.amazonaws.com/' + designer_id + '/' + files.filename

    if upload_file(files.filename, 'darksnow', designer_id):
        current = datetime.now()
        image_info = DesignerImageMap(
            timestamp=current.strftime("%Y-%m-%d %H:%M:%S"),
            image_url=image_url,
            image_name=files.filename
        )
        designer.data.append(image_info)
        designer.timestamp = datetime.now().timestamp()
        designer.save()
        logging.info('image data updated to db')
        return True
    else:
        return False


def upload_file(file_name, bucket, object_name):
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, '%s/%s' % (object_name, file_name))
        logging.info('image uploaded to s3 successfully')
    except ClientError as e:
        logging.error(e)
        logging.info('image unsuccessful updation')
        return False
    return True


def recent_data(designer_id: str):
    for item in DesignerModel.designer_index.query(designer_id, scan_index_forward=False, limit=1):
        print(item.first_name)
        return item

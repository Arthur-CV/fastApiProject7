from db1.database import engine
from fastapi import FastAPI
from sqlalchemy.engine.base import Engine
from enum import Enum
from typing import Optional
from fastapi import APIRouter, Query, Body, Path, Depends
from pydantic import BaseModel
from db1 import models

app = FastAPI(
    title="Office Management App"
)


@app.get('/Office/{id}/comment', tags=['Put the products on the shelf'])
def index():
    return {'message': 'Put the products on the shelf'}


class StorageType(str, Enum):
    Shelf_1 = 'Shelf_10kg'
    Shelf_2 = 'Shelf_20kg'
    Shelf_3 = 'Shelf_30kg'


@app.get('/office/storage/{type}/comment', tags=['Select_shelf'])
def get_storage_type( Shelf: StorageType):
    return {'message': f'storage type {type}'}


class Assortment(str, Enum):
    coffee = 'coffee'
    cookies = 'cookies'
    add = 'other'


@app.post('/office/storage/{type}/comment', tags=['Select_product'])
def post_assortment(Assortment: Assortment):
    return {'message': f'assortment {type}'}


@app.post('/office/{worker}/put_products/{put}/comment', tags=['Office_worker_put_products'])
def post_comment(Maks_Office_worker: Optional[str] = None, Kate_Office_worker2: Optional[str] = None, Mark_Office_worker3: Optional[str] = None):
        """
        - **username**
        """


class Workname(BaseModel):
  Name: str
  Role: str
  published: Optional[bool]

def required_functionality():
    return {'message': 'Learning Fastapi is important'}


# models.Base.metadata.create_all(engine)




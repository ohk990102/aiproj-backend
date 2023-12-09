from typing import Generic, Literal, TypeVar, Union
from uuid import uuid4

import aiofiles
from fastapi import APIRouter, Depends, File, Form, Header, HTTPException, UploadFile

from models.db import db_session, Model
from pydantic import BaseModel
from utils import convert_datetime, convert_size

router = APIRouter(prefix="/models", tags=["models"])

ResultType = TypeVar("ResultType")


class ResultSuccessClass(BaseModel, Generic[ResultType]):
    status: Literal["success"]
    result: ResultType


class ResultErrorClass(BaseModel):
    status: Literal["error"]
    message: str


class ModelResponse(BaseModel):
    id: str
    name: str
    size: str
    created_at: str
    updated_at: str


@router.get("/")
async def get_models() -> Union[
    ResultSuccessClass[list[ModelResponse]], ResultErrorClass
]:
    result = Model.query.all()
    result = [
        ModelResponse(
            id=model.id,
            name=model.name,
            size=convert_size(model.size),
            created_at=convert_datetime(model.created_at),
            updated_at=convert_datetime(model.updated_at),
        )
        for model in result
    ]

    return {"status": "success", "result": result}


class ModelCreateResponse(BaseModel):
    id: str


@router.post("/new")
async def new_model(
    name: str = Form(...), model: UploadFile = File(...)
) -> Union[ResultSuccessClass[ModelCreateResponse], ResultErrorClass]:
    model_id = str(uuid4())

    async with aiofiles.open(f"static/models/{model_id}", "wb") as f:
        await f.write(model.file.read())
        size = await f.tell()

    model_obj = Model(id=model_id, name=name, size=size)
    db_session.add(model_obj)
    db_session.commit()

    return {"status": "success", "result": {"id": model_id}}


@router.get("/{model_id}")
async def get_model(model_id: str):
    model = Model.query.filter_by(id=model_id).first()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return {"status": "success", "result": model}

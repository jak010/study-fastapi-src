from __future__ import annotations

from typing import TypeVar, Generic

from fastapi.routing import APIRouter
from pydantic.generics import GenericModel

member_router = APIRouter(tags=['Member'])

T = TypeVar("T")


class ResponseBaseModel(GenericModel, Generic[T]):
    status: int = 200
    code: int = 20000
    data: T

    class Config:
        @staticmethod
        def schema_extra(schema, model):
            """
            :param schema:
                {'title': 'MemberEntity', 'type': 'object', 'properties': {'age': {'title': 'Age', 'type': 'integer'}, 'name': {'title': 'Name', 'type': 'string'}, 'password': {'title': 'Password', 'type': 'string'}, 'profile': {'$ref': '#/components/schemas/MemberProfile'}}, 'required': ['age', 'name', 'password']} <class 'src.controller.member.MemberEntity'>
            """

            schema_properties = schema.get("properties", {})

            hidden_fields = []
            for k, v in schema_properties.items():
                if "password" == k:
                    hidden_fields.append(k)

            for field in hidden_fields:
                if field in schema_properties:
                    del schema["properties"][field]
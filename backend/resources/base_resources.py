from typing import Type
from backend.dao.base_dao import BaseDao
from flask_restful import Resource
from flask import request


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type) -> None:
        self.__dao = dao
        self.__model_type = model_type
        super().__init__()

    def get(self, id=None):
        if id:
            return self.__dao.read_by_id(id)

        return self.__dao.read_all()

    def post(self):
        data = request.json
        model = self.__model_type(**data)

        return self.__dao.save(model)

    def put(self, id):
        data = request.json

        if data['id'] == id:
            model = self.__dao.read_by_id(id)
            for key, value in data.items():
                setattr(model, key, value)

            return self.__dao.save(model)

        return None, 404

    def delete(self, id):
        model = self.__dao.read_by_id(id)
        self.__dao.delete(model)

        return None, 204

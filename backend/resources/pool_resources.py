from backend.models.pool import Pool
from backend.dao.pool_dao import PoolDao
from flask_restful import abort, fields, marshal_with
from flask import jsonify
from backend.resources.base_resources import BaseResource
from backend.resources.rules import Rules


class PoolResources(BaseResource):
    fields = {
        "id": fields.Integer,
        "fk_product": fields.Integer,
        "fk_seller": fields.Integer,
        "fk_category": fields.Integer,
        "approved": fields.Boolean
    }

    def __init__(self) -> None:
        self.__dao = PoolDao()
        self.__model_type = Pool
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        try:
            if Rules().check_model():
                return super().post()
        except Exception as erro:
            return abort(jsonify(cod_error='401',
                                 detail=erro.args))

    @ marshal_with(fields)
    def put(self, id: int):
        return super().put(id)

    @ marshal_with(fields)
    def delete(self, id: int):
        return super().delete(id)

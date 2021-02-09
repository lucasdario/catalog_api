from flask_restful import Resource


class BaseResource(Resource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return 'Retornando GET'

    def post(self):
        return 'Retornando POST'

    def put(self):
        return 'Retornando PUT'

    def delete(self,):
        return 'Retornando DELETE'

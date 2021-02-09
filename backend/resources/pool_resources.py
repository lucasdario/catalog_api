from backend.resources.base_resources import BaseResource


class PoolResources(BaseResource):
    def __init__(self) -> None:
        super().__init__()

    def get(self):
        return super().get()

    def post(self):
        return super().post()

    def put(self):
        return super().put()

    def delete(self):
        return super().delete()

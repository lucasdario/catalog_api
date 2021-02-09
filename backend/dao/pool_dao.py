from backend.dao.base_dao import BaseDao
from backend.models.pool import Pool


class PoolDao(BaseDao):
    def __init__(self) -> None:
        self.__type_model = Pool
        super().__init__(self.__type_model)

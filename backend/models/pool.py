from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import validates
import sys
sys.path.append('.')
from backend.models.base_model import BaseModel
from backend.utils.validators import validate_type


class Pool(BaseModel):
    __tablename__ = 'pool'
    fk_product = Column(Integer, nullable=False)
    fk_seller = Column(Integer, nullable=False)
    fk_category = Column(Integer, nullable=False)
    approved = Column(Boolean, nullable=False, default=False)

    def __init__(self, fk_product: int, fk_seller: int, fk_category: int, approved: bool = False) -> None:
        self.fk_product = fk_product
        self.fk_seller = fk_seller
        self.fk_category = fk_category
        self.approved = approved

    @validates('fk_product')
    def valdiate_fk_product(self, key, fk_product):
        fk_product = validate_type(fk_product, int, key)
        return fk_product

    @validates('fk_seller')
    def valdiate_fk_seller(self, key, fk_seller):
        fk_seller = validate_type(fk_seller, int, key)
        return fk_seller

    @validates('fk_category')
    def validate_fk_category(self, key, fk_category):
        fk_category = validate_type(fk_category, int, key)
        return fk_category

    @validates('approved')
    def validate_approved(self, key, approved):
        approved = validate_type(approved, bool, key)
        return approved

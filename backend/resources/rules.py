import re
from flask import request
from sqlalchemy.sql.functions import mode
from backend.models.pool import Pool
from backend.models.fake_product_model import ProductModel
from backend.models.fake_seller_model import SellerModel
from backend.models.fake_category_model import CategoryModel


class Rules():
    def check_model(self) -> bool:
        data = request.json
        model = Pool(**data)

        model_product = ProductModel().instance_obj(model.fk_product)
        model_seller = SellerModel().instance_obj(model.fk_seller)
        model_category = CategoryModel().instance_obj(model.fk_category)

        self.check_product(model_product)
        self.check_seller(model_seller)
        self.check_category(model_category)

        return True

    def check_product(self, model: ProductModel):
        improper_word = ['arma', 'gun', 'sexy', 'alcool']

        if not model.name:
            raise ValueError('Name can not empty')
        if len(model.name) < 50:
            raise ValueError('The name cannot be less than 50')
        for word in improper_word:
            if re.search(word, model.name, re.IGNORECASE):
                raise ValueError('Improper word detected in name')

        if not model.description:
            raise ValueError('Description can not empty')
        if len(model.description) < 100:
            raise ValueError('The description cannot be less than 100')
        for word in improper_word:
            if re.search(word, model.description, re.IGNORECASE):
                raise ValueError('Improper word detected in description')

        if model.price < 14.99:
            raise ValueError('Price cannot be less than R$14,99')

        try:
            sum_of_dimensions = model.width + model.height + model.length
            if sum_of_dimensions < 29 or sum_of_dimensions > 200:
                raise ValueError('Dimensions invalid')
        except Exception as error:
            raise error

        if model.weight > 10:
            raise ValueError('Weight invalid')

    def check_seller(self, model: SellerModel):
        if len(model.name) > 50:
            raise ValueError('The name cannot be greater than 50')
        if not model.active:
            raise ValueError('The seller is not enabled')

    def check_category(self, model: CategoryModel):
        improper_word = ['armas', 'Agrotóxicos', 'sexy', 'alcool']

        for word in improper_word:
            if re.search(word, model.name, re.IGNORECASE):
                raise ValueError('Improper word detected in category')

import re
from flask import request
from backend.models.pool import Pool
from backend.models.fake_product_model import ProductModel


class Rules():
    def check_model(self) -> bool:
        data = request.json
        model = Pool(**data)

        model_product = ProductModel().instance_obj(model.fk_product)

        self.check_product(model_product)
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

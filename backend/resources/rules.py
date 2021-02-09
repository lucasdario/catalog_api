import re
from flask import request
from backend.models.pool import Pool
from backend.models.fake_product_model import ProductModel


class Rules():
    def check_model(self):
        data = request.json
        model = Pool(**data)

        model_product = ProductModel().instance_obj(model.fk_product)
        result = self.check_product(model_product)
        return result

    def check_product(self, model: ProductModel):
        improper_word = ['arma', 'gun', 'sexy', 'alcool']

        if not model.name:
            return 'Name can not empty'
        if len(model.name) < 50:
            return 'The name cannot be less than 50'
        for word in improper_word:
            if re.search('\\'+model.name+'\\b', word, re.IGNORECASE):
                return 'Improper word detected'

        if not model.description:
            return 'Description can not empty'
        if len(model.description) < 100:
            return 'The description cannot be less than 100'
        for word in improper_word:
            if re.search(r"\\"+model.description+"\\b", word, re.IGNORECASE):
                return 'Improper word detected'

        if model.price < 14.99:
            return 'Price cannot be less than R$14,99'

        try:
            sum_of_dimensions = model.width + model.height + model.length
            if sum_of_dimensions < 29 or sum_of_dimensions > 200:
                return 'Dimensions invalid'
        except Exception as error:
            return error

        if model.weight > 10:
            return 'Weight invalid'

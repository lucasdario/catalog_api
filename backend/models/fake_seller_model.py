class SellerModel():
    def __init__(self, id: int = None, name: str = None, active: bool = None) -> None:
        self.id = id
        self.name = name
        self.active = active

    def instance_obj(self, op):
        obj = object

        if op == 1:
            obj = SellerModel(1, 'João do Eletronico', True)
        elif op == 2:
            obj = SellerModel(2, 'Maria da Tecnologia', False)
        elif op == 3:
            obj = SellerModel(3, 'Casa de embalagens', True)

        return obj

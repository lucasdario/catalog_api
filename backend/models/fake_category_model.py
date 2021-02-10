class CategoryModel():

    def __init__(self, id: int = None, name: str = None, description: str = None) -> None:
        self.id = id
        self.name = name
        self.description = description

    def instance_obj(self, op):
        obj = object

        if op == 1:
            obj = CategoryModel(1, 'Telefonia', 'Teste1')
        elif op == 2:
            obj = CategoryModel(2, 'Informatica', 'Teste2')
        elif op == 3:
            obj = CategoryModel(3, 'Armas', 'Teste3')

        return obj

class CategoryModel():
    def __init__(self, id: int, name: str, description: str) -> None:
        self.id = id,
        self.name = name,
        self.description = description

    def instance(op):
        obj = object
        if op == 1:
            obj = CategoryModel(1, 'Telefonia', 'Telefonia Mobile')
        elif op == 2:
            obj = CategoryModel(2, 'Informatica', 'Acessorios')

        return obj

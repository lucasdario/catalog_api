class ProductModel():

    def __init__(self, id: int = None, sku: str = None, name: str = None, description: str = None,
                 price: float = None, height: float = None, width: float = None,
                 length: float = None, weight: float = None) -> None:
        self.id = id
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight

    def instance_obj(self, op: int):
        obj = object
        if op == 1:
            obj = ProductModel(1, '1234567891234', 'Smartphone Samsung Galaxy A10s Dual Chip Android 9.0 Tela 6.2” Octa-Core 32GB 4G Câmera 13MP+2MP - Azu',
                               'O Galaxy A10s possui design confortável que se encaixa perfeitamente em suas mãos. O acabamento elegante e moderno se destaca, \
                           e você ainda pode escolher entre as cores preta, azul ou vermelha. Para desbloqueá-lo,\
                                basta posicionar o seu dedo no leitor de digital na parte de trás.', 1200.99, 150.9, 75.8, 7.5, 0.800)
        elif op == 2:
            obj = ProductModel(2, '9874563214569', 'Mouse óptico Dell - MS116 (PRETO)  (MODELO -  54654545446546545468)',
                               'O mouse óptico Dell™ – MS116 fornece rastreamento óptico de LED e conectividade com fio,\
                                   interdum vestibulum mattis mi netus est ipsum id augue,interdum vestibulum mattis mi netus est ipsum id augue,\
                                       interdum vestibulum mattis mi netus est ipsum id augue,interdum vestibulum mattis mi netus est ipsum id augue,\
                                    além de oferecer performance excelente todos os dias.', 78.99, 80.9, 50.8, 5.5, 5)
        elif op == 3:
            obj = ProductModel(3, '9513578963256', 'Teclado Gamer - mode gun (MODELO -  6654684454687)',
                               'Teclado gamer com mode de ativação rápida de arma, teste de validação de palavras imprópriasinterdum vestibulum mattis mi netus est ipsum id augue,\
                                    urna lacinia tincidunt laoreet congue cubilia imperdiet praesent, nisl\
                                         lobortis fringilla convallis curabitur etiam ullamcorper. ', 550.88, 100.9, 30.8, 4.5, 0.890)

        return obj

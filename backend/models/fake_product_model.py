class ProductModel():

    def __init__(self, id: int, sku: str, name: str, description: str,
                 price: float, height: float, width: float,
                 length: float, weight: float) -> None:
        self.id = id
        self.sku = sku
        self.name = name
        self.description = description
        self.price = price
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight

    def instance(op: int):
        obj = object
        if op == 1:
            obj = ProductModel(1, '1234567891234', 'Smartphone Samsung Galaxy A10s Dual Chip Android 9.0 Tela 6.2” Octa-Core 32GB 4G Câmera 13MP+2MP - Azu',
                               'O Galaxy A10s possui design confortável que se encaixa perfeitamente em suas mãos. O acabamento elegante e moderno se destaca, \
                           e você ainda pode escolher entre as cores preta, azul ou vermelha. Para desbloqueá-lo,\
                                basta posicionar o seu dedo no leitor de digital na parte de trás.', 1200.99, 156.9, 75.8, 7.5, 800)
        elif op == 2:
            obj = ProductModel(2, '9874563214569', 'Mouse óptico Dell - MS116 (PRETO)',
                               'O mouse óptico Dell™ – MS116 fornece rastreamento óptico de LED e conectividade com fio,\
                                    além de oferecer performance excelente todos os dias.', 78.99, 80.9, 50.8, 5.5, 250)

        return obj

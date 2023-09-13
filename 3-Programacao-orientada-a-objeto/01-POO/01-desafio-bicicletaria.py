class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor        


    def buzinar(self):
        print('buzina!!!')
    
    def parar(self):
        print('parando a bike')
        print('bike parada')

    def correr(self):
        print('taka le pau marco veio!!!')

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta('vermelha', 'caloi 10', 2022, 1000)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('verde', 'monark', 2000, 189)

Bicicleta.buzinar(b2)
b2.buzinar()
print (b2.cor)
print(b2)



class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('inicializando a classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self): #destrutor só executa ao final da execução
        print('removendo a instancia da classe')
        
    def falar(self):
        print('auau!!!')
    


c = Cachorro ('pincher', 'caramelo')
c.falar()

print('texto')
print('texto')
del c #força o destrutor a qualquer momento
print('texto')
print('texto')
print('texto')
print('texto')

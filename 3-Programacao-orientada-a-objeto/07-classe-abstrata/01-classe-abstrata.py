from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod #obriga o uso do metodo da classe pai
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('liga tv')

    def desligar(self):
        print('desliga tv')
    
    @property
    def marca(self):
        return "Samsung"

class ControleAr(ControleRemoto):
    def ligar(self):
        print('liga ar')

    def desligar(self):
        print('desliga ar')
    
    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleAr()
controle.ligar()
controle.desligar()
print(controle.marca)




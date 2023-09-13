class Passaro:
    def voar(self):
     print('Voando...')   

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestrus não voa')

# FIXME: exemplo ruim do uso de herança para "gnhar" o metodo voar 

class Aviao(Passaro):
    def voar(self):
        print('Levantando voo...')

def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
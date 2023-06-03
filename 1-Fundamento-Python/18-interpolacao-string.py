
nome = 'Luan'
idade = 35
prifissão = 'Programador'
linguagem = 'Python'
saldo = 45.698

dados = {'nome': 'Luan', 'idade': 35}

print('Nome: %s Idade: %d' % (nome, idade))
print('Nome: {} Idade: {}' .format(nome, idade))
print('Nome: {0} Idade: {1}' .format(nome, idade))
print('Nome: {nome} Idade: {idade}' .format(nome=nome, idade=idade))
print('Nome: {nome} Idade: {idade}' .format(**dados))

print(f'nome: {nome} Idade: {idade}')
print(f'nome: {nome} Idade: {idade} Saldo: {saldo:.2f}')

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Informe sua idade: '))

if idade >= MAIOR_IDADE:
    print('Você é maior e pode tirar CNH')

if idade < MAIOR_IDADE:
    print('Você é menor e não pode tirar CNH')

if idade >= MAIOR_IDADE:
    print('Você é maior e pode tirar CNH')
else:
    print('Você é menor e não pode tirar CNH')

if idade >= MAIOR_IDADE:
    print('Você é maior e pode tirar CNH')
elif idade == IDADE_ESPECIAL:
    print('Você pode fazer as aulas teoricas porem não pode tirar CNH ainda')
else:
    print('Você é menor e não pode tirar CNH')
    
    

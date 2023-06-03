'''opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair \n: '))

    if opcao == 1:
        print('Sacando')
    elif opcao == 2:
        print('Extrato')
else:
    print('Obrigado')'''

'''while True:
    numero = int(input('informe o numero: '))

    if numero == 10:
        break
    print(numero)
'''

'''for numero in range(30):
    
    if numero == 10:
        break

    print(numero, end=' ')
'''

'''for numero in range(30):
    
    if numero == 10:
        continue

    print(numero, end=' ')
'''

while True:
    numero = int(input('Digite um numero: '))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue
    
   
    
    print(numero) 

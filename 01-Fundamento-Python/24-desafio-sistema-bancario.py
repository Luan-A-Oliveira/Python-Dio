menu = '''

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_DE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        print('Deposito')
        deposito = float(input('Qual valor deseja deposita: ')) 
        if deposito < 0 :
            print('valor de deposito invalido tente um valor positivo')
        else:
            saldo += deposito
            extrato += f'Deposito: R$ {deposito:.2f}\n'       

    elif opcao == '2':
        print('Saque')
        valor_saque = float(input('Digite o valor a ser sacado: '))
        if numero_saques > LIMITE_DE_SAQUE:
            print(f'Você ultrapassou o limite de saques diarios, que é de {LIMITE_DE_SAQUE}' )

        elif valor_saque > 500:
            print('Valor maximo de saque é R$500,00')

        elif valor_saque > saldo:
            print('Saldo insuficiente')

        else:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f'Saque: R$ {valor_saque:.2f}\n'
   
    elif opcao == '3':
        print('Extrato')
        print(extrato)
        

    elif opcao == '4':
        break

    else:
        print('Opção inválida, selecione uma das opções.')


''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
def analisar_nivel_energia(energia):
    if 100 <=  energia <= 100000:
        if energia <= 8000:
            return "Inseto!"
        else:
            return "Mais de 8000!"

# leitura do numero de criaturas a serem testadas
C = int(input('Numero de teste: '))

# testanto energia das criaturas
for i in range(C):
    # entrada do valor de energia
    N = int(input('Energia da criatura: '))

    # testando a criatura 
    resultado = analisar_nivel_energia(N)
    print(resultado)
    ''' 
    TODO Leia as as entradas e crie as condições necessárias para verificar se é maior ou
    menor do que 8000 e imprima "Inseto!" ou "Maior que 8000!" para cada caso.
    '''
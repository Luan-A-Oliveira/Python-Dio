''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
T = int(input())

for i in range(T):
    if 1 <= T <= 10000:
        N = int(input())
        K = int(input())
        count = 0
        while N >= K:
            N-K
        count =+ 1
        resultado = count + N
        print(resultado)


    ''' 
    TODO Ler as variáveis de entrada N e K. Talvez seja necessário fazer um "split" na linha 
         para obtenção dos valores.
    TODO Calcular e imprimir o número de garrafas que o cliente terá no segundo dia, se 
         aproveitar ao máximo a oferta.
    '''
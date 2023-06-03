''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
import sys

N = int(input())
while(N > 0):

    ent = sys.stdin.readline()


    A = ent.split()[0]
    B = ent.split()[1]
    
    if str(A).endswith(str(B)):
        print('encaixa')
    else:
        print('não encaixa')
    
    N = N - 1
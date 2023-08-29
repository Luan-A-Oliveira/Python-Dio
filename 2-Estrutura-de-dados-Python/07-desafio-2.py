'''A primeira linha de entrada contém inteiro T (1 ≤ T ≤ 10000) , que indica o número de casos de teste. 
Em cada uma das T linhas a seguir vêm dois inteiros N e K (1 ≤ K, N ≤ 10000), 
 respectivamente o número de refrigerantes comprados e o número de garrafas vazias para ganhar uma cheia'''

''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
#definir a quantidade de testes
T = int(input()) 

#criar lista para guardar os valores de cada teste 
resultados = []

#iniciar os testes
for i in range(T):
  N, K = map(int, input().split())
  #definir o total de garrafas e o tanto que é necessário para trocar
  total_garrafas = N
  troca = K
  
  #para cada iteração, realizar o teste
  if N>=K:
    total_trocas = total_garrafas // troca
    sobra = total_garrafas % troca
    resultado = total_trocas + sobra
    resultados.append(resultado)
  else:
    resultados.append(total_garrafas)

#imprimir os resultados um por linha
for i in resultados:
  print(i, sep='\n')


  ''' 
    TODO Ler as variáveis de entrada N e K. Talvez seja necessário fazer um "split" na linha 
         para obtenção dos valores.
    TODO Calcular e imprimir o número de garrafas que o cliente terá no segundo dia, se 
         aproveitar ao máximo a oferta.
  '''
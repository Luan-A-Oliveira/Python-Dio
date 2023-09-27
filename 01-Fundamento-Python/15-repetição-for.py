
#texto = input('Informe o texto: ')

texto = ""

VOGAIS = "AEIOU"

#iteravel

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:
    print() #adiciona quebra de linha

#range

for numero in range(0, 51, 5):
    print(numero, end=' ')
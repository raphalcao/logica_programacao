
numeros = []
resultado = []
confirma = False

while True:
    array_numero = input('Digite um número ou aperte 0 para sair:')
    if array_numero.isnumeric() == True:
        if array_numero == '0':
            break
        numeros.append(int(array_numero))
    else:
        print('Digite um número válido.')

alvo = 0
alvo = input("Digite um número para ser resultado de soma:")

while not alvo.isnumeric():
    alvo = input("Digite um número para ser resultado de soma: ")
alvo = int(alvo)



for n in numeros:
    if confirma:
        break


    indexA = numeros.index(n)
    indexB = numeros.index(n) + 1

    while indexB < len(numeros):
        resultado.append(n + numeros[indexB])

        if alvo in resultado:
            confirma = True
            print(indexA, indexB)
            break
        indexB += 1

if not confirma:
    print('Não houve resultado!')
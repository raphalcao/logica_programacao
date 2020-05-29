
numeros = []
resultado = []
success = False

while True:
    array_numero = input('Digite um número ou aperte 0 para sair:')
    if array_numero.isnumeric() == True:
        if array_numero == '0':
            break
        numeros.append(int(array_numero))
    else:
        print('Digite um número válido.')

alvo = 0
alvo = input("Digite um número para localizar a soma específica:")

while not alvo.isnumeric():
    alvo = input("Digite um número. ")
alvo = int(alvo)



for n in numeros:
    if success:
        break


    indexA = numeros.index(n)
    indexB = numeros.index(n) + 1

    while indexB < len(numeros):
        resultado.append(n + numeros[indexB])

        if alvo in resultado:
            success = True
            print(indexA, indexB)
            break
        indexB += 1

if not success:
    print('Não houve resultado!')
arrayBloco = []
blocoAgua = 0

qtde_bloco = int(input('Quantidade de blocos no eixo X: '))



while len(arrayBloco) < qtde_bloco:
    blocoCasa = input( 'Número de blocos na casa {}: '.format(len(arrayBloco)+1))
   
    if blocoCasa.isnumeric() and int(blocoCasa) >= 0:
        arrayBloco.append(int(blocoCasa))
    else:
        print('Por favor, insira um número inteiro e não negativo')

for posicaoArrayBloco in range(1, len(arrayBloco)+1):

    ultimaPosicao = -1
    valorIndexInicial = 0
    valorUltimoIndex = 0

    for v in arrayBloco:
        if v >= posicaoArrayBloco:
            break
        valorIndexInicial += 1

    for x in range(valorIndexInicial, len(arrayBloco)):
        if x == qtde_bloco:
            valorIndexInicial = 0
            valorUltimoIndex = 0
            break
        elif arrayBloco[ultimaPosicao] >= posicaoArrayBloco:
            valorUltimoIndex = len(arrayBloco)+ultimaPosicao
            break
        else:
            ultimaPosicao -= 1

    for index in range(valorIndexInicial, valorUltimoIndex):
        if arrayBloco[index] < posicaoArrayBloco:
            blocoAgua += 1

print(f'Quantidade de blocos: {blocoAgua}')
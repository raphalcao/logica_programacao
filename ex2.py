dados = input('Digite os pares de brackets: ').strip()
tamanho = len(dados)

bracketsAbertura = [
    '[', '(', '{'
]

bracketsFechamento = [
    ']', ')', '}'
]

condicao = True
indexVariavelSaida = 1


def verificaTamanho(a):
    if a % 2 != 0:
        return False


for d in dados:

    indexVariavelEntrada = dados.index(d)

    verificaTamanho(tamanho)
   

    if indexVariavelEntrada < (tamanho / 2) and condicao:
        if d in bracketsAbertura:
            indexVariavelEntrada += 1
        else:
            condicao = False
            break

    elif indexVariavelEntrada < tamanho and condicao:
        if d in bracketsFechamento:
           
            x = dados[dados.index(d)-indexVariavelSaida]
            if x in bracketsAbertura:
                indexBracketsAbertura = bracketsAbertura.index(x)
            if d in bracketsFechamento:
                indexBracketsFechamento = bracketsFechamento.index(d)

            if indexBracketsAbertura != indexBracketsFechamento:
                condicao = False

            indexVariavelEntrada += 1
            indexVariavelSaida += 2

        else:
            condicao = False
            break

if condicao:
    print('SIM')
else:
    print('NÃO')




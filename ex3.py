valor_array_entrada = []

dia_compra = -1
melhor_dia = 0

qtde_dia = input('Digite o número de dias para a análise: ')
while not qtde_dia.isnumeric():
    qtde_dia = input('Insira a quantidade de dia(s): ')
qtde_dia = int(qtde_dia)

for c in range(qtde_dia):
    valor_qtde_dia = input('Valor em dias {}: '.format( len(valor_array_entrada)+1 ))
    while not valor_qtde_dia.isnumeric():
        valor_qtde_dia = input('Insira o dia em número {}: '.format(len(valor_array_entrada) + 1))
    valor_array_entrada.append(int(valor_qtde_dia))

while dia_compra >= qtde_dia or dia_compra < 0:
    dia_compra = input('Dia de compra da loja: ')
    dia_compra = int(dia_compra)-1

for c in range(dia_compra+1, len(valor_array_entrada)):
    resultado_valor = valor_array_entrada[c] - valor_array_entrada[dia_compra]
    if resultado_valor > melhor_dia:
        melhor_valor = valor_array_entrada[c]
        melhor_dia = resultado_valor

if melhor_dia > 0:
    dia_venda = valor_array_entrada.index(melhor_valor)
    print("Melhor dia: {}   Lucro obtido: {}".format(dia_venda+1, melhor_dia))

else:
    print("Não deve fazer transação")
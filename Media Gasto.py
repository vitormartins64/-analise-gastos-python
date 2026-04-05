# Dados de gastos

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08, 4821.37, 934.82, 7610.05, 2509.64, 9999.99, 1047.28, 6382.11, 7205.76, 3150.40, 8873.92, 412.58, 5698.23, 7781.67, 2304.15, 6902.84, 1555.55, 8340.09, 4701.33, 2987.70, 6123.48 ]

# Calculamos a media encontrando o valor total de gastos com sum
# e a quantidade total de compras realizadas com len

total_gastos = sum(gastos)
quantidade_compras = len(gastos)
media_gastos = total_gastos / quantidade_compras
# Resultado

print(f'A media de gastos e {media_gastos} reais')

# Dados de Gastos

gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08 ]
# Variavel que vai contar quantas compras foram feitas acima de 3000

contador_acima_3000 = 0
for gasto in gastos:
    if gasto > 3000:
        contador_acima_3000 +=1
# Quantidade de compras

quantidade_compras = len(gastos)

#  Conseguimos calcular a porcentagem de valores acima de 3000 entre todas as compras

porcentagemn__acima_3000 = (contador_acima_3000 / quantidade_compras) * 100
# Resultado


print(f'{contador_acima_3000} compras foram feitas acima de R$3000,00.')
print(f'{porcentagemn__acima_3000} % dos gastos foram acima de R$3000,00')
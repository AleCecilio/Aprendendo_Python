compras =  (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)


totais = tuple(map(lambda c: c['quantidade'] * c['preco'], compras))

print(f'Proços totais: {totais}')
print(f'Total Geral: {sum(totais)}')

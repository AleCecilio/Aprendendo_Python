compras =  (
    {'quantidade': 2, 'preco': 10},
    {'quantidade': 3, 'preco': 20},
    {'quantidade': 5, 'preco': 14},
)


def cal_total(c): return c['quantidade'] * c['preco']


totais = tuple (map(cal_total, compras))

print(f'Proços totais: {totais}')
print(f'Total Geral: {sum(totais)}')

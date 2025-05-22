def calc_preco_final(preco_bruro, calc_imposto, *params):
    return preco_bruro + preco_bruro* calc_imposto(*params)


def imposto_x(importado):
    return 0.22 if importado else 0.3


def imposto_y(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, imposto_x, True)
    preco_final = calc_preco_final(preco_final, imposto_y,True, 1.5)
    print(f'Preço Final do Produto: R$ {preco_final}')

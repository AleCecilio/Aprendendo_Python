def execultar(funcao):
    if callable(funcao):
        funcao()


def bom_dia():
    print('Bom Dia!')


def boa_tarde():
    print('Boa Tarde!')


if __name__ == '__main__':
    execultar(bom_dia)
    execultar(boa_tarde)
    execultar(1)

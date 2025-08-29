'''
Bônus: Programação Funcional
 Receba lista de números.
 Use map para dobrar, filter para múltiplos de 5 e reduce para somar.
 Use lambda para tudo.
'''
from functools import reduce


if __name__ == '__main__':
    numeros = [1,23,5,6,50,85,9,10,11,12,13]
    print(f'\nNúmeros = {numeros}')
    print(f'Dobrar Números = {list(map(lambda x: x*2, numeros))}')
    print(f'Filtrar Múltiplos de 5 = {list(filter(lambda x: x % 5 == 0,numeros))}')
    print(f'Reduce para Somar = {reduce(lambda x,y: x + y, numeros)}\n')
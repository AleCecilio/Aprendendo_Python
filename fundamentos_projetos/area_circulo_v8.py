#!python
from math import pi


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    raio = input('Digite o raio: ')
    area = circulo(raio)
    print('A area do circulo eh:', area,'\n')
    
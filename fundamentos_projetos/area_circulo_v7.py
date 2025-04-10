#!python
from math import pi


def circulo(raio):
    print(f'A area da circunferencia de raio {raio} eh:\n {pi} * {raio}^2 = ', pi*float(raio)**2,'\n')


if __name__ == '__main__':
    raio = input('Digite o raio: ')
    circulo(raio)

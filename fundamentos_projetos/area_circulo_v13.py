from math import pi
import sys
import errno


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print('Eh necessario informar o raio do circulo. \nSintaxe: {} <raio>'.format(sys.argv[0][2:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric(): # Nesse caso o 'isnumeric()' não aceita float. Mais pra frente o try/except  será a auternativa mais útil pra essa situação, mas como o curso ainda não passo por isso, deixarei assim.
        help()
        print('O raio deve ter valor numerico!')
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('A area do circulo eh:', area,'\n')

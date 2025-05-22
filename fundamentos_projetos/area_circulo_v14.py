from math import pi
import sys
import errno

class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'

def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print(f'Eh necessario informar o raio do circulo. \nSintaxe: {sys.argv[0][2:]} <raio>')
    # Mudei aqui para ficar mais condisente com o PEP8


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric(): # O 'isnumeric()' não aceita float. O try/except é a auternativa mais útil pra essa situação, mas como o curso ainda não encinou por isso, deixarei assim.
        help()
        print(
            TerminalColor.ERRO 
            + 'O raio deve ter valor numerico!' 
            + TerminalColor.NORMAL
        )
        sys.exit(errno.EINVAL)

    raio = sys.argv[1]
    area = circulo(raio)
    print('A area do circulo eh:', area,'\n')

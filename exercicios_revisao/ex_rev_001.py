'''
 Exercício 1: Estatísticas de Arquivo Numérico
 Leia um arquivo texto com números (um por linha), armazene-os em uma lista e calcule:
 - Soma
 - Média
 - Maior e menor valor
 - Quantos pares e ímpares
'''
import os


def soma(num):
    return sum(num)


def media(num):
    return soma(num) / len(num)


def maior_menor (num):
    return (max(num),min(num))


def num_par_impar(num):
    n_pares = sum(i for i in num if i % 2 == 0)
    n_impares = sum(i for i in num if i % 2 != 0)
    return (n_pares,n_impares)


if __name__ == '__main__':
    numeros = []
    with open('numeros.csv') as arquivo:
        for linha in arquivo:
            numeros.append(int(linha.strip()))
        
    print(f'\n{os.getcwd()}\n')
    print(f'Soma: {soma(numeros)}')
    print(f'Média: {media(numeros):.2f}')
    print(f'Maior: {maior_menor(numeros)[0]}')
    print(f'Menor: {maior_menor(numeros)[1]}')
    print(f'Número de valores pares: {num_par_impar(numeros)[0]}')
    print(f'Número de valores impares: {num_par_impar(numeros)[1]}')
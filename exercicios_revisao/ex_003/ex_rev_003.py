'''
 Exercício 3: Calculadora Matemática Avançada
 Permita soma, subtração, multiplicação, divisão, potência, resto, fatorial.
'''


import math
import sys


# --- Funções de entrada ---
def verificar_Float(prompt):
    while True:
        try:
            valor = float(input(prompt)) 
            break
        except ValueError:
            print('Digite um valor válido')
    
    return valor


def receber_Dois_valores():
    print('Digite os Valores:')
    x = verificar_Float('-> ')
    y = verificar_Float('-> ')
    return x, y
    

def receber_Um_valor():
    print('Digite o Valor:')
    n = verificar_Float('-> ')
    return n


# --- Operações matemáticas ---
def soma(*args):
    return sum(args)


def subtracao(x,y):
    return x - y


def multiplicacao (x, y):
    return x * y


def divisao (x, y):
    return x / y


def potencia (x, y):
    return pow(x, y)


def resto(x, y):
    return x % y


def fatorial(x):
    return math.factorial(x)


# --- Função auxiliar para continuar operação ---
def teste_Resultado(resultado, funcao):
    if resultado == None:
        n1, n2 = receber_Dois_valores()
        resultado = funcao(n1,n2)
    else:
        n1 = resultado
        n2 = receber_Um_valor()
        resultado = funcao(n1,n2)

    return n1, n2, resultado


# --- Impressão de resultados ---
def implimir_Resultado(n1, n2=None, resultado=None, operacao=None):
    print('RESULTADO: ')
    if operacao == '!':
        print(f'{n1}{operacao} = {resultado}')
    else:
        print(f'{n1} {operacao} {n2} = {resultado}')


# --- Calculadora ---
def calculadora(resultado=None):
    print('CALCULADORA!!!')
    
    print('\nDigite a operação:')
    print('Digite (+) para Adição')
    print('Digite (-) para Subtração')
    print('Digite (x) para Multiplicação')
    print('Digite (/) para Divisão')
    print('Digite (^) para Potência')
    print('Digite (%) para Resto da Divisão')
    if resultado == None: 
        print('Digite (!) para Fatoração')

    while True:
        try:
            operacao = input('Operação: -> ').strip()
            if operacao not in {'+','-','x','/','^','%','!'}:
                print('Digite uma operação válida!')
                continue
            break
        except ValueError:
            print('Digite um caracter válido!')

    match operacao:
        case '+':
            n1, n2, resultado = teste_Resultado(resultado,soma)
            implimir_Resultado(n1, n2, resultado, operacao)
        case '-':
            n1, n2, resultado = teste_Resultado(resultado,subtracao)
            implimir_Resultado(n1, n2, resultado, operacao)
        case 'x':
            n1, n2, resultado = teste_Resultado(resultado,multiplicacao)
            implimir_Resultado(n1, n2, resultado, operacao)
        case '/':
            n1, n2, resultado = teste_Resultado(resultado,divisao)
            implimir_Resultado(n1, n2, resultado, operacao)
        case '^':
            n1, n2, resultado = teste_Resultado(resultado,potencia)
            implimir_Resultado(n1, n2, resultado, operacao)
        case '%':
            n1, n2, resultado = teste_Resultado(resultado,resto)
            implimir_Resultado(n1, n2, resultado, operacao)
        case '!':
            n = math.trunc(receber_Um_valor())
            resultado = fatorial(n)
            implimir_Resultado(n, resultado, operacao)
        
    return resultado


# --- Menu interativo ---
def menu(resultado):
    if resultado == None:
        resultado = calculadora()
    
    while True:
        print('O que deseja fazer?')
        print('(1) Continuar Operação')
        print('(2) Iniciar Nova Operação')
        print('(3) Sair da Calculadora')

        while True:
            try:
                op = int(input('-> '))
                if op not in {1,2,3}:
                    print('Digite uma opção válida!')
                    continue
                break
            except ValueError:
                print('Digite um valor válido!!!')
        
        match op:
            case 1:
                resultado = calculadora(resultado)
            case 2:
                resultado = calculadora()
            case 3:
                sys.exit('Programa Finalizado!!!')
        
        return resultado


# --- Execução ---
if __name__ == '__main__':
    menu(calculadora())

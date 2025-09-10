# Minhas Proprias resoluções 
'''
# 1° Solução encontarda (é a pior) (não funcional)
def mdc(lista):
    divisor =  min(lista)
    
    divisiveis = list(filter(lambda x: x % divisor == 0, lista)) # desnecessario
    
    if divisiveis == lista:
        return divisor
    else:
        lista_aux = lista # desnecessario
        lista_aux.append(divisor-1) # modifica a lista (não é imutavel)
        return mdc(lista_aux)
'''


'''
# 2° Solução encontrada (não funcional) \
    # (tem a limitação da recursividade, além de ser mais extenso)
def mdc(lista, divisor=None):
    if divisor is None:
        divisor = min[lista]
    
    if all(num % divisor == 0 for num in lista):
        return divisor
    else:
        return mdc(lista, divisor - 1)
'''


'''
# 3° Solução Encontrada (não funcional) \
    # (tem a limitação da recursividade)
def mdc(lista):
    divisor =  min(lista)
    
    while divisor > 0:
        if all(num % divisor == 0 for num in lista):
            return divisor
        divisor -= 1
'''


'''
# 4° Solução encontrada (não funcional) 
# Nesse caso é apenas um ex. de aplicação no código, \
    # o ideal é utilizar o "math.gcd()" diretamente no "print".
from math import gcd
from functools import reduce

def mdc(lista):
    return reduce(gcd, lista)
'''


# Resolução do Curso (é a melhor nesse contexto) (funcional)
def mdc(numeros): 
    def calc(divisor):
        return divisor if sum(map (lambda x: x % divisor, numeros)) == 0 \
            else calc(divisor - 1)
    return calc(min(numeros))


if __name__ == '__main__':
    print(mdc([21, 7])) #7
    print(mdc([125, 5])) #5
    print(mdc([9, 594, 66, 3])) #3
    print(mdc([55, 22])) #11
    print(mdc([15, 150])) #15
    print(mdc([7, 9])) #1
    
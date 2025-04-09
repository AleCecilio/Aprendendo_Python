
#PRIMEIROS EXEMPLOS
'''
print('Primeiro Programa')
print(1+2)'
'''

#TIPOS BASICOS
'''
print('True')
print('False')
print(1.2 + 1)
print('Aqui eu falo na minha lingua!')
print('Tb funciona!')
print('Voce eh' + 3 * 'muito ' + 'legal!')
#print(3 + '3') -> ambiguidade
print([1, 2, 3]) #list
print({'nome' : 'Alessandro', 'idade' : 21})
print(None)'
'''

#VARIAVEIS 
'''
a = 2
b = 5.2
print(a + b)

a = 'Agora eu sou string!'
print(a)

#print(a + b)
'''

#OPERADORES ARITMETICOS
'''
print(2 + 1)
print(3 - 1)
print(2 * 2)
print(5 ** 2)
print(4 / 2)
print(8.3 // 4)
print(5 % 2)
'''

#OPERADORES RELACIONAIS
'''
print(3 > 4)
print(4 >= 3)
print(1 < 2)
print(3 <= 1)
print(3 != 2)
print (3 == 3)
print (3 == '3')'
'''

#OPERADOS DE ATRIBUIÇÃO
'''
a = 3
a = a + 7
print(a)

a += 5
print(a)

a -= 3
print(a)

a *= 2
print(a)

a /= 4
print(a)

a %= 4
print(a)

a **= 8
print(a)

a //= 127
print(a)
'''

#OPERADORES LOGICOS
'''
print(True or False)
print(7 != 3 and 2 > 3)
#Tabela Verdade do AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#Tabela Verdade do OR
print(True or True)
print(True or False)
print(False or True)
print(False or False)

#Tabela Verdade do XOR
print(True != True)
print(True != False)
print(False != True)
print(False != False)

#Operador de negação (unario) 
print(not True)
print(not False)

print(not 0)
print(not 1)
print(not not -1)
print(not not True)

#Cuidado! Operadores Bit-a-bit
print(True & False)
print(True | False)
print(True ^ False)

#AND Bit-a-bit
#3 = 11
#2 = 10
#_ = 10
print(3 & 2)

#OR Bit-a-bit
#3 = 11
#2 = 10
#_ = 11
print(3 | 2)

#XOR Bit-a-bit
#3 = 11
#2 = 10
#_ = 01
print(3 ^ 2)

#Um Pouco de Realidade 
saldo = 1000
salario = 4000
despesas = 2967

meta = saldo > 0 and salario - despesas >= 0.2 * salario
print(meta)
'''

#OPERADORES TERNARIOS
'''
roupas_molhadas = True

print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[roupas_molhadas])
print('Hoje estou com as roupas ' + ('molhadas.' if roupas_molhadas else 'secas.')) 
'''

#MAIS OPERADORES 
'''
#Operador do Membro
lista = {1, 2, 3, 'Ana', 'Carla'}
print(2 in lista)
print('Ana' not in lista)

#Operador de Indentidade
x = 3
y = x 
z = 3

print(x is y)
print(x is z)
print(x is not z)'


lista_a = {1, 2, 3}
lista_b = lista_a
lista_c = {1, 2, 3}

print(lista_a  is lista_b)
print(lista_a is lista_c)
print(lista_c is not lista_a)
'''


#BUILTINS
'''
print(type(1))
__builtins__.print(__builtins__.type('Fala Galera'))
#__builtins__.help(__builtins__.dir)

#import math
#print(dir())
print(dir(__builtins__))'
'''

#CONVERSÃO DE TIPOS
'''
print(2 + 3)
print('2' + '3')
print(2 + '3')

a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b))
print(str(a) + b)

print(type(str(a)))
'''

#COERÇÃO AUTOMATICA
'''
print(10 / 2)
print(type(10 / 2))
print(10 / 3)
print(10 // 3)
print(type(10 // 3))
print(10 // 3.3)
print(type(10 // 3.3))
print(2 + True)
print(2 + False)
'''

#TIPOS NUMERICOS 1
'''
print(dir(int))
print(dir(float))

a = 5
b = 2.5

print(a / b)
print(a + b)

print(b.is_integer())
print(5.0.is_integer())

print(int.__add__(2, 3))
print((-2).__abs__())
print(abs(-2))
'''

#TIPOS NUMERICOS 2
'''
print(2.2 + 1.1)

from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))


print(Decimal(1) / Decimal(7))

print(Decimal.max(Decimal(1), Decimal(7)))

from decimal import Decimal, getcontext
getcontext().prec = 2
print(Decimal(2.2) + Decimal(1.1))
'''

#STINGS 1
'''
nome = "Saulo Pedro"
print(nome)
print(nome[0])

#nome[0] = 'P' errp!! Não pode ser mudada

#print('Marca d'agua)

print("Marca d'agua")
print('Marca d\'agua")

texto = 'Texto entre apostrofos pode ter "aspas"'

doc = """Texto com multipla
    ... linhas"""

print('Texto com multipla\n\t... linhas')
'''

#STRINGS 2
'''
nome = 'Ana Paula'

print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[-5:])
print(nome[:3])
print(nome[2:5])

numeros = '123456789'
print(numeros)
print(nuemros[::])
print(nuemros[::2])
print(nuemros[1::2])
print(nuemros[::-1])
print(nuemros[::-2])

print(nome::-1)
'''

#STRINGS 3
'''
frase = 'Python é uma linguagem excelente'
print('py' in frase)
print('ing' in frase)
print(len(frase))
print(frase.lower())
print(frase.upper())

frase = frase.upper()
print(frase)

print(frase.split())
print(frase.split('E'))
'''

#STRINGS 4 
'''
a = '123'
b = ' de Oliveira 4'
print(a + b)
print(a.__add__(b))
print(str.__add__(a,b))


print(len(a))
print(a.__len__())

print('1' in a)
print(a.__contains__('1'))
'''

#LISTAS 1
'''
lista = []
print(type(lista))
print(len(lista))

lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = [1, 5, "Ana", "Bia"]
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)

nova_lista.reverse()
print(nova_lista)
'''

#LISTAS 2 
''' 
lista = [1, 5, "Rebeca", "Guilherme", 3.1415]
print(lista.index("Guilherme"))
print(lista[2])

print("Rebeca" in lista)
print("Pedro" not in lista)

print(lista[1])
print(lista[-1])'
'''

#LISTAS 3
'''
lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])
del lista[2]
print(lista)
del lista[1:]
print(lista)
'''

#TUPLAS
'''
tupla = tuple()
tupla = ()

print(type(tupla))

tupla = ('um',)
print(type(tupla))

print(tupla[0])

cores = ('verde', 'amarelo', 'azul', 'branco')

print(cores[0])
print(cores[1:])
print(cores[-1])

print(cores.index('amarelo'))
print(cores.count('azul'))'
'''

#DICIONARIOS 1
'''
pessoa = {'nome':'Prof(a) Ana', 'idade':38, 'cursos' : ['Ingles' , 'Portugues']}
print(type(pessoa))

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'][1])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
'''

#DICIONARIOS 2
'''
pessoa = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React','Python']}
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
print(pessoa)

print(pessoa.pop('idade'))

print(pessoa)
pessoa.update({'idade' : 40, 'sexo':'M'})
print(pessoa)

del pessoa['cursos']
print(pessoa)

pessoa.clear()
print(pessoa)
'''

#CONJUNTO
'''
a = {1, 2, 3}
print(type(a))

a = set('codddd3r')
print(a)

print({1,2,3} == {3,2,1,3})

c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)

print(c2 <= c1)
print(c1 >= c2)

print({1, 2, 3} - {2})
print(c1 - c2)

c1 -= {2}
print(c1)'
'''

#INTERPOLACAO
'''
from string import Template

nome, idade = 'Ana', 30
print('Nome: %s Idade: %d' % (nome, idade)) #mais antiga
print('Nome: {0} Idade: {1}'.format(nome, idade)) #python <  3.6
print(f'Nome: {nome} Idade: {idade}') #python >= 3.6

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))'
'''

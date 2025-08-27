'''
Exercício 5: Recursão e Funções Anônimas
 Crie uma função recursiva para fatorial.
 Outra para MDC.
 Use lambda e map para elevar ao quadrado.
 Use filter para números ímpares.
 Use List Comprehension para pares
'''

# --- Fatorial Recursivo ---
def fatorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return (num * fatorial(num-1))
    

# --- MDC Recursivo ---
def MDC(n1, n2):
    if n2 == 0:
        return n1
    else:
        return MDC(n2, n1 % n2)


if __name__ == '__main__':
   lista = [1,2,3,4,5,6,7,8,9]

   print(f'\n{fatorial(5)}')
   print(MDC(4,2))
   print(f'\n{list(map(lambda x: x**2,lista))}')
   print(f'\n{list(filter(lambda x: x % 2 != 0, map(lambda x: x**2,lista)))}')
   print([x**2 for x in lista if x**2 % 2 == 0])

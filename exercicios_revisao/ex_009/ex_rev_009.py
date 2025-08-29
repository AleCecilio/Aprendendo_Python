'''
 Exercício 9: Decorator de Logging
 Crie um decorator log que mostre a chamada de função, argumentos e retorno.
 Ex:
 @log
 def soma(a, b): return a + b
'''


# --- Decorator Log ---
def log(funcao):
    def decorator(*args,**kwargs):
        print(f'Início da Chamada da Função: {funcao.__name__}')
        print(f'args: {', '.join(map(str,args))}')
        print(f'kwargs: {kwargs}')
        resultado = funcao(*args,**kwargs)
        print(f'Resultado: {resultado}')
        return resultado
    return decorator

# --- Função De Soma ---
@log
def soma(x,y):
    return x + y

if __name__ == '__main__':
    print(soma(5, y=3))
'''
 Exercício 8: Manipulação de Argumentos
 Função que recebe parâmetros fixos, *args e **kwargs.
 Opera soma, média ou produto.
 Use unpacking para listas e dicionários
'''
import f_entradas

# --- Caculando Valores ---
def calcular(*args,**kwargs):
    kwargs.get('op')
    match op:
        case 1:
            return sum(args)
        case 2: 
            return sum(args)/len(args) if args else 0
        case 3:
            mult = 1
            for n in args:
                mult *=n
            return mult


# --- Execução ---
if __name__ == '__main__':
    lista = []

    print('Digite uma Opção: ')
    print('1 - Soma')
    print('2 - Média')
    print('3 - Produto')

    op = f_entradas.verifica_Int('-> ', 1, 3)
    dicionario = {
        'op' : op
    }

    cont = 0

    while True:
        print('Digite um valor: ')
        lista.append(f_entradas.verifica_Int(('-> ')))
        cont +=1
        if cont == 1:
            print('Digite o segundo Valor: ')
            lista.append(f_entradas.verifica_Int(('-> ')))
        print('Deseja Digitar mais Números?')
        print('0 - Não')
        print('1 - Sim')
        op_loopin = f_entradas.verifica_Int('-> ', 0, 1)

        match op_loopin: 
            case 0:
                break
            case 1:
                continue


    print(calcular(*lista, **dicionario))
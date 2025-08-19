with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome : {},  Idade : {}'.format(*pessoa), file = saida)

    
if arquivo.closed:
    print('O Arquivo foi fechado!')

if saida.closed:
    print('O Arquivo de saida foi fechado!')
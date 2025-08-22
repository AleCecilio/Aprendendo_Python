'''
 Exercício 2: Cadastro de Clientes com Tupla, Dicionário e Arquivo
 Permita cadastrar clientes via input(), armazenando cada cliente como um dicionário com nome,
 idade e cidade.
 Grave os dicionários em uma lista e depois em um arquivo CSV.
 Permita pesquisar por nome ou cidade e editar pelo índice.
'''

#Além das Funções Incompletas Há também a necessidade de baixar o texto do arquivo para edita-lo se o usuario quiser 

import csv 
import sys
import errno

def menu_Principal (pessoas):
    while True: 
        print('Menu\n')
        print('(1) Adicionar Pessoa\n')
        print('(2) Salvar e Sair\n')
        print('(3) Pesquisar por Nome\n')
        print('(4) Pesquisar por Cidade\n')
        print('(5) Editar Pessoa\n')
        print('(6) Sair\n')

        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        match op:
            case 1:
                adicionar_Pessoas(pessoas)
            case 2:
                salvar_CSV(pessoas)
                encerrar_programa()
            case 3:
                pesquisa_Nome(pessoas)
            case 4:
                pesquisa_Cidade(pessoas)
            case 5:
                editar_Pessoa(pessoas)
            case 6:
                encerrar_programa()


def adicionar_Pessoas (pessoas):
    pessoa = {
        'nome' : input(f'Digite o nome da {i+1}° pessoa: '),
        'idade' : input(f'Digite a idade da {i+1}° pessoa: '),
        'cidade' : input(f'Digite a cidade da {i+1}° pessoa: ')
    }
    pessoas.append(pessoa)
    print('Pessoa Cadastrada com Sucesso!')


def salvar_CSV (pessoas):
    try: 
        with open('pessoas.csv', 'w', newline='', encoding='utf-8') as saida:
            escritor = csv.DictWriter(saida, fieldnames=['nome', 'idade', 'cidade'])
            escritor.writerows(pessoas)
    except OSError as e:
        if e.errno == errno.EACCES:
            print("Erro: Sem permissão para salvar o arquivo.")
        elif e.errno == errno.ENOSPC:
            print("Erro: Disco cheio, impossível salvar o arquivo.")
        elif e.errno == errno.EROFS:
            print("Erro: Sistema de arquivos somente leitura.")
        else:
            print(f"Erro ao salvar o arquivo: {e}")

    if saida.closed:
        print('Arquivo Salvo com Sucesso!')


def encerrar_programa():
    sys.exit('Encerrando Programa...')


def pesquisa_Nome(pessoas):


def pesquisa_Cidade(pessoas):


def editar_Pessoa(pessoas):


if __name__ == '__main__':
    pessoas = []
    menu_Principal(pessoas)
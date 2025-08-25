'''
 Exercício 2: Cadastro de Clientes com Tupla, Dicionário e Arquivo
 Permita cadastrar clientes via input(), armazenando cada cliente como um dicionário com nome,
 idade e cidade.
 Grave os dicionários em uma lista e depois em um arquivo CSV.
 Permita pesquisar por nome ou cidade e editar pelo índice.
'''


import csv 
import sys
import errno


def verifica_Int(prompt, min_val=None, max_val=None):
    while True:
        try:
            valor = int(input(prompt))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print(f'Digite um número entre {min_val} e {max_val}.')
                continue
            return valor
        except ValueError:
            print('Digite um número válido!')


def verificar_String(prompt):
    string = input(prompt).strip()
    while string == '':
        print('Esse campo não pode ficar vazio!')
        string = input('Digite novamente: ').strip()
    return string


def exibir_Pessoa(pessoa):
    print(f"Nome : {pessoa['nome']}, Idade : {pessoa['idade']}, Cidade : {pessoa['cidade']}, Id : {pessoa['id']}")
    

def ler_Arquivo(pessoas):
    try:
        with open('pessoas.csv', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for row in leitor: 
                row['idade'] = int(row['idade'])
                row['id']=  int(row['id'])
                pessoas.append(row)
    except FileNotFoundError:
        print('Ainda Não Há Pessoas Cadastradas !!!')


def menu_Principal (pessoas):
    while True: 
        print('Menu\n')
        print('(1) Adicionar Pessoa\n')
        print('(2) Pesquisar por Nome\n')
        print('(3) Pesquisar Por Id\n')
        print('(4) Pesquisar por Cidade\n')
        print('(5) Editar Pessoa\n')
        print('(6) Excluir Pessoa\n')
        print('(7) Salvar e Sair\n')
        print('(0) Sair Sem Salvar\n')

        op = verifica_Int("Escolha uma opção: > ", 0, 7)

        match op:
            case 1:
                adicionar_Pessoas(pessoas)
            case 2:
                pesquisa_Nome(pessoas)
            case 3:
                pesquisar_Id(pessoas)
            case 4:
                pesquisa_Cidade(pessoas)
            case 5:
                editar_Pessoa(pessoas)
            case 6:
                excluir_Pessoa(pessoas)
            case 7:
                salvar_CSV(pessoas)
                encerrar_Programa()
            case 0:
                encerrar_Programa()


def adicionar_Pessoas (pessoas):
    print('ADICIONAR PESSOA\n')
    id = max([p['id'] for p in pessoas], default=-1)+1

    nome = verificar_String('Digite o nome da pessoa: ')
    idade = verifica_Int('Digite a Idade da Pessoa: > ', 0)
    cidade = verificar_String('Digite a cidade da pessoa: ')

    pessoa = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade,
        'id': id
    }
    pessoas.append(pessoa)
    print(f'Pessoa Registrada Com o Id: {id}')
    print('Pessoa Cadastrada com Sucesso!')


def pesquisa_Nome(pessoas):

    print('PESQUISA POR NOME\n')
    nome = verificar_String('Digite o nome: ')
    encontrado = False

    for i, pessoa in enumerate(pessoas):
        if nome.lower() == pessoa['nome'].lower():
            exibir_Pessoa(pessoa)
            encontrado =True
        
    if not encontrado:
        print(f'O nome {nome} não está registrado!!!')


def pesquisar_Id(pessoas):
    print('PESQUISAR POR ID:\n')
    id_busca = verifica_Int('Digite o ID da Pessoa: > ', 0)
    
    for pessoa in pessoas:
        if id_busca == pessoa['id']:
            exibir_Pessoa(pessoa)
            return pessoa
            
    print(f'Não Existe Pessoa Registrada Com ID: {id_busca}')
    return None


def pesquisa_Cidade(pessoas):
    print('PESQUISA POR CIDADE\n')
    cidade = verificar_String('Digite a cidade: ')
    encontrado = False
    nPessoas_cidade = 0

    for pessoa in pessoas:
        if cidade.lower() == pessoa['cidade'].lower():
            exibir_Pessoa(pessoa)
            encontrado = True
            nPessoas_cidade +=1
        
    if not encontrado:
        print(f'Nenhuma pessoa registrada mora em {cidade}!!!')
    else: 
        print(f'Número de moradores em {cidade}: {nPessoas_cidade}')    


def editar_Pessoa(pessoas):
    print('EDITAR PESSOA\n')
    pessoa = pesquisar_Id(pessoas)
    if pessoa is not None:

        print('Digite o que deseja editar:\n')
        print('(1) Nome\n')
        print('(2) Idade\n')
        print('(3) Cidade\n')
        print('(4) Editar Tudo\n')
        
        op = verifica_Int("Escolha uma opção: > ", 1, 4)

        match op:
            case 1: 
                pessoa['nome'] = verificar_String('Digite o nome da pessoa: ')
                print('Nome Editado!!!')
            case 2: 
                pessoa['idade'] = verifica_Int('Digite a Idade da Pessoa: > ', 0)
            case 3:
                pessoa['cidade'] = verificar_String('Digite a cidade da pessoa: ')
                print('Cidade Editada!!!')
            case 4:
                pessoa['nome'] = verificar_String('Digite o nome da pessoa: ')
                pessoa['idade'] = verifica_Int('Digite a Idade da Pessoa: > ', 0)
                pessoa['cidade'] = verificar_String('Digite a cidade da pessoa: ')
                print('Pessoa Editada!!!')

        print('Pessoa Após a Edição:\n')
        exibir_Pessoa(pessoa)


def excluir_Pessoa(pessoas):
    print('EXLUIR PESSOA:\n')
    pessoa = pesquisar_Id(pessoas)
    if pessoa is None:
        print("Pessoa não encontrada. Voltando ao menu...")
        return

    print('Confimar Exclusão?\n')
    print('(1) Para Excluir')
    print('(2) Para Não Excluir\n')

    op = verifica_Int("Escolha uma opção: > ", 1, 2)

    match op:
        case 1: 
            pessoas.remove(pessoa)
            print('A Pessoa Foi Excluída')
        case 2: 
            print('Voltando ao Menu')


def salvar_CSV (pessoas):
    try: 
        with open('pessoas.csv', 'w', newline='', encoding='utf-8') as saida:
            escritor = csv.DictWriter(saida, fieldnames=['nome', 'idade', 'cidade', 'id'])
            escritor.writeheader()
            escritor.writerows(pessoas)
            print('Arquivo salvo com sucesso!')
    except OSError as e:
        if e.errno == errno.EACCES:
            print("Erro: Sem permissão para salvar o arquivo.")
        elif e.errno == errno.ENOSPC:
            print("Erro: Disco cheio, impossível salvar o arquivo.")
        elif e.errno == errno.EROFS:
            print("Erro: Sistema de arquivos somente leitura.")
        else:
            print(f"Erro ao salvar o arquivo: {e}")


def encerrar_Programa():
    sys.exit('Encerrando Programa...')


if __name__ == '__main__':
    pessoas = []
    ler_Arquivo(pessoas)
    menu_Principal(pessoas)

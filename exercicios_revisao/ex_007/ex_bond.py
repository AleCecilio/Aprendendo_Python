'''
Perdoem-me o nome do arquivo, mas era inevitável, afinal é 007.
Exercício 7: Sistema de Vendas
Cadastre produtos (nome, preço, quantidade) em dicionário.
Calcule valor total de compras.
Use comprehension para listar estoques baixos.
Grave e leia dados de arquivo CSV
'''

import csv
import f_entradas
import errno
import sys


# --- Leitura dos Arquivos de Produtos ---
def ler_Produtos(produtos):
    try: 
        with open('produtos.csv', newline='', encoding='utf-8') as arquivo1:
            leitor = csv.DictReader(arquivo1)
            for linha in leitor:
                linha['id'] = int(linha['id'])
                linha['preco'] = float(linha['preco'])
                linha['quantidade'] = int(linha['quantidade'])
                produtos.append(linha)
    except FileNotFoundError:
        print( 'Ainda Não Há Produtos Cadastrados!!!')


# --- Leitura dos Arquivos de Estoque ---
def ler_Estoque (estoque_baixo):
    try:
        with open('estoque_baixo.csv', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                linha['quantidade'] = int(linha['quantidade'])
                estoque_baixo.append(linha)
    except FileNotFoundError:
        print('Não Há Produtos Com Estoque Baixo!!!')


# --- Escrevendo Produtos No Arquivo ---
def escrever_Produtos(produtos):
    try:
        with open('produtos.csv', 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=['nome', 'id', 'preco', 'quantidade'])
            escritor.writeheader()
            escritor.writerows(produtos)
            print('\nArquivo salvo com sucesso!')
    except OSError as e:
        if e.errno == errno.EACCES:
            print("\nErro: Sem permissão para salvar o arquivo.")
        elif e.errno == errno.ENOSPC:
            print("\nErro: Disco cheio, impossível salvar o arquivo.")
        elif e.errno == errno.EROFS:
            print("\nErro: Sistema de arquivos somente leitura.")
        else:
            print(f"\nErro ao salvar o arquivo: {e}")


# --- Escrevendo Estoque No Arquivo ---
def escrever_Estoque(estoque_baixo):
    try:
        with open('estoque_baixo.csv', 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=['nome', 'id', 'quantidade'])
            escritor.writeheader()
            escritor.writerows(estoque_baixo)
            print('\nArquivo salvo com sucesso!')
    except OSError as e:
        if e.errno == errno.EACCES:
            print("\nErro: Sem permissão para salvar o arquivo.")
        elif e.errno == errno.ENOSPC:
            print("\nErro: Disco cheio, impossível salvar o arquivo.")
        elif e.errno == errno.EROFS:
            print("\nErro: Sistema de arquivos somente leitura.")
        else:
            print(f"\nErro ao salvar o arquivo: {e}")


# --- Checando se o Estoque está baixo ---
def checar_Estoque(produto, estoque_baixo):
    if produto['quantidade'] < 5:
        encontrado = False
        for p in estoque_baixo:
            if p['id'] == produto['id']:
                p['quantidade'] = produto['quantidade']  
                encontrado = True
                break
        if not encontrado:
            baixo =  {
                'nome': produto['nome'],
                'id': produto['id'],
                'quantidade': produto['quantidade']
            }
            estoque_baixo.append(baixo)


# --- Cadastro de Produto ---
def cadastrar_produtos(produtos, estoque_baixo):
    print('\n--- CADASTRO DE PRODUTOS ---')
    nome = f_entradas.verifica_String('Digite o nome do Produto: ')

    id = max([p['id'] for p in produtos], default=999) + 1
    print(f'ID do Produto: {id}')

    preco = f_entradas.verificar_Float('Digite o valor do Produto R$(xx.xx): ')

    quant = f_entradas.verifica_Int('Digite a quantidade em Estoque: ', 0)
    
    produto = {
        'nome' : nome,
        'id' : id,
        'preco': preco,
        'quantidade' : quant
    }
    
    try:
        produtos.append(produto)
        checar_Estoque(produto, estoque_baixo)
        print('Usuário Salvo com Sucesso!!!')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')


# --- Calcaulando o Valor Total de Compras ---
def calcular_Compras(produtos, estoque_baixo):
    print('\n--- COMPRAS ---')
    total_compra = 0  
    
    while True:
        nome = f_entradas.verifica_String('Digite o nome do Produto: ')
        
        produto_encontrado = next((p for p in produtos if p['nome'].lower() == nome.lower()), None)
        
        if not produto_encontrado:
            print(f"\nProduto '{nome}' não encontrado.")
            continue
        
        quant = f_entradas.verifica_Int('Digite a Quantidade: ', 1)
        
        if quant > produto_encontrado['quantidade']:
            print(f"\nEstoque insuficiente! Disponível: {produto_encontrado['quantidade']} unidades.")
            continue
        
        produto_encontrado['quantidade'] -= quant   

        checar_Estoque(produto_encontrado, estoque_baixo)     

        total_parcial = quant * produto_encontrado['preco']
        total_compra += total_parcial
        print(f'Compra parcial: {total_parcial} | Total acumulado: {total_compra}')
        
        
        print('\nEscolha uma opção:')
        print('(1) Continuar Comprando')
        print('(2) Efetuar Compra')
        print('(3) Cancelar Compra')
        
        op = f_entradas.verifica_Int('-> ', 1, 3)
        
        match op:
            case 1:
                continue
            case 2:
                print(f'\nCompra efetuada com sucesso! Valor total: R${total_compra:.2f}')
                return
            case 3:
                for p in produtos:
                    p['quantidade'] += quant if p['nome'].lower() == nome.lower() else 0
                print('\nCompra cancelada.')
                return


# --- Finalizar Programa ---
def encerrar_Programa():
    print('\nEncerrando Programa...')
    sys.exit('Programa Finalizado!!!')

# --- Menu ---
def menu(produtos, estoque_baixo):
    while True:
        print('\n--- MENU ---')
        print('(1) Cadastrar Produto')
        print('(2) Comprar Produtos')
        print('(3) Sair e Salvar')
        print('(4) Sair Sem Salvar')

        op = f_entradas.verifica_Int('-> ',1,4)

        match op:
            case 1:
                cadastrar_produtos(produtos, estoque_baixo)
            case 2:
                calcular_Compras(produtos, estoque_baixo)
            case 3:
                escrever_Produtos(produtos)
                escrever_Estoque(estoque_baixo)
                encerrar_Programa()
            case 4:
                encerrar_Programa()
            
                
# --- Execução ---
if __name__ == '__main__':
    produtos = []
    estoque_baixo = []
    ler_Produtos(produtos)
    ler_Estoque(estoque_baixo)
    menu(produtos, estoque_baixo)


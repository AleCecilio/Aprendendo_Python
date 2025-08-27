'''
 Exercício 4: Sistema de Login Simples
 Cadastre usuários (nome e senha) usando dicionário.
 Armazene em arquivo.
 Permita login com verificação.
 Criptografe as senhas (ex: string invertida).
 Use decorator para checar login antes de certas funções.
'''

import csv
import errno
import hashlib
import sys
import f_entradas


# --- Decorator Para Checar Login ---
def requer_login(funcao):
    def protecao (*args, **kwargs):
        if not args[0]:
            print("Você precisa estar logado para usar essa função!")
            return None
        return funcao(*args, **kwargs)
    return protecao


# --- Ler os Usuários do Arquivo ---
def ler_Arquivo (usuarios): 
    try:
        with open('usuarios.csv', newline='', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                linha['id'] = int(linha['id'])
                usuarios.append(linha) 
    except FileNotFoundError:
        print('Ainda não há Usuários Cadastrados!!!')


# --- Salvar Novos Usuários ---
@requer_login
def escrever_arquivo (usuaruio_logado, usuarios):
    try:
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=['id', 'nome', 'senha'])
            escritor.writeheader()
            escritor.writerows(usuarios)
            print('\nArquivo salvo com sucesso!')
            return True
    except OSError as e:
        if e.errno == errno.EACCES:
            print("\nErro: Sem permissão para salvar o arquivo.")
        elif e.errno == errno.ENOSPC:
            print("\nErro: Disco cheio, impossível salvar o arquivo.")
        elif e.errno == errno.EROFS:
            print("\nErro: Sistema de arquivos somente leitura.")
        else:
            print(f"\nErro ao salvar o arquivo: {e}")
        return False


# --- Finalizar a Execução do Programa ---
def sair_Programa():
    sys.exit('Encerrando Programa!!\n')


# --- Criptografar A Senha ---
def criptografar_Senha(senha):
    hash_senha = hashlib.sha256(senha.encode())
    senha = hash_senha.hexdigest()
    return senha


# --- Cadastro de Usuários ---
def cadastro_Usuarios(usuarios):
    print('\nCADASTRO DE USUÁRIOS')

    nome = f_entradas.verifica_String('Nome de Usuário: ')

    senha = criptografar_Senha(f_entradas.verificar_Senha())

    id = (max([u['id'] for u in usuarios], default=99) + 1) 
    print(f'O ID do Usuário {nome} é: {id}!')
    
    usuario = {
        'id' : id,
        'nome' : nome,
        'senha' : senha
    }

    try:
        usuarios.append(usuario)
        print('Usuário Salvo com Sucesso!!!')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')


# --- Fazer Login ---
def fazer_Login(usuarios):
    print('\nLogin De Usuário')
    tentativas = 0
    autenticado = None
    while tentativas < 3:
        nome = f_entradas.verifica_String('Nome de Usuário: ')
        senha = criptografar_Senha(f_entradas.verificar_Senha())
        for usuario in usuarios:
            if usuario['nome'].lower() == nome.lower() and usuario['senha'] == senha:
                autenticado = usuario
                break
        if autenticado:
            print('\nLogin Efetuado Com Sucesso!!!')
            print(f"Seja Bem Vindo, {autenticado['nome']}!")
            return autenticado
        else:
            tentativas +=1
            print(f'Usuário ou senha inválidos! Tentativa {tentativas}/3')

    print('Você exedeu o número de tentativas!!!')
    return None


# --- Mostra os Dados Do Usuário Atual ---
@requer_login
def mostrar_dados(usuario_logado):
    print('\nDados do Usuário')
    print(f"Nome: {usuario_logado['nome']}")
    print(f"ID: {usuario_logado['id']}")


# --- Menu Principal --- 
def menu(usuarios):
    usuario_logado = None
    while True:
        print('\nMENU')
        print('Digite uma Opção')
        print('(1) Cadastrar Usuário')
        print('(2) Fazer Login')
        print('(3) Mostrar Dados Do Usuário')
        print('(4) Sair e Salvar')
        print('(5) Sair sem Salvar')
        op = f_entradas.verifica_Int('Opção: -> ',1,5)

        match op:
            case 1:
                cadastro_Usuarios(usuarios)
            case 2:
                usuario_logado = fazer_Login(usuarios)
            case 3:
                mostrar_dados(usuario_logado)
            case 4:
                if escrever_arquivo(usuario_logado, usuarios):
                    sair_Programa()
            case 5: 
                sair_Programa()


# --- Execução --- 
if __name__ == '__main__':
    usuarios = []
    ler_Arquivo(usuarios)
    menu(usuarios)

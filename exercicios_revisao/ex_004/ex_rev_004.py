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
import re
import hashlib


# --- Ler os Usuários do Arquivo ---
def ler_Arquivo (usuarios): 
    try:
        with open('usuarios.csv', newline='', ecolding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                linha['id'] = int(linha['id'])
                usuarios.append(linha) 
    except FileNotFoundError:
        print('Ainda não há Usuários Cadastrados!!!')


# --- Salvar Novos Usuários ---
def ecrever_arquivo (usuarios):
    try:
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=['id', 'nome', 'senha'])
            escritor.writeheader()
            escritor.writerow(usuarios)
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


# --- Vefica se a String é Válida ---
def verifica_String(prompt):
    string = input(prompt).strip()
    while string == '':
        print(f'o campo {string} não pode estar vazio!!!')
        string = input(prompt).strip()
    return string


# --- Criptografar A Senha ---
def criptografar_Senha(senha):
    hash_senha = hashlib.sha256(senha.encode())
    senha = hash_senha.hexdigest()
    return senha


# -- Verifica se a Senha é Válida ---
def vericar_Senha():
    while True:
        senha = verifica_String('Senha (Númros, Letras e Símbolos): -> ')
        if len(senha) < 6 or len(senha) > 6:
            print('A Senha deve ter 6 caracteres.')
        elif not re.search(r"[A-Z]", senha):
            print("A senha deve ter pelo menos uma letra maiúscula.")
        elif not re.search(r"[0-9]", senha):
            print("A senha deve ter pelo menos um número.")
        elif not re.search(r"[!@#$%^&*()_+=\-]", senha):
            print("A senha deve ter pelo menos um símbolo especial.")
        else: 
            break
    senha = criptografar_Senha(senha)
    return senha


# --- Cadastro de Usuários ---
def cadatro_Usuarios(usuarios):
    print('CADASTRO DE USUÁRIOS')
    nome = verifica_String('Nome de Usuário: ')
    senha = vericar_Senha()
    id = 100 + (max([u['id'] for u in usuarios], default=0) + 1)
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
    print('Login De Usuário')


'''
O que falta?
Fazer a fazer_Login, o main, se o login etiver incorreto 3 vezes deve retornar um erro e bloquear o sistema e sair.

Lembrete:
    No ex 003 devo analisar o uso do @log
'''
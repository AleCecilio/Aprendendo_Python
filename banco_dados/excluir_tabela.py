from bd import nova_conexao
from mysql.connector import ProgrammingError


try:
    with nova_conexao() as conexao:
        try:
            cursor =  conexao.cursor()
            cursor.execute('DROP TABLE IF EXISTS emails')
        except ProgrammingError as e:
            print(f'Erro {e.msg}')    

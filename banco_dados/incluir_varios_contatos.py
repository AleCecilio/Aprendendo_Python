from mysql.connector.errors import ProgrammingError
from bd import nova_conexao 


sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '96765-4321'),
    ('Bia', '97765-4321'),
    ('Luca', '89765-4321'),
    ('Lu', '95765-4321'),
    ('Gui', '93765-4321'),
    ('Beca', '92765-4221'), 
    ('Pedro', '98765-4721')
)


with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram inclídos {cursor.rowcount} registro!')
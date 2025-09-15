from mysql.connector import connect

conexao = connect (
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'Moreira9922!'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Banco de Dados {i}: {database[0]}')
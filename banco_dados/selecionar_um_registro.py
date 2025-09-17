from bd import nova_conexao

sql = 'SELECT tel, nome FROM contatos LIMIT 1 OFFSET 1'

with nova_conexao() as conexao:
    cursor = conexao.cursor()
    cursor.execute(sql)
    
    print(cursor.fetchone())
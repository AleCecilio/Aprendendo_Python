lista = [1, 2, 3]
dobro = map(lambda x: x * 2, lista)
print(list(dobro))


lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

so_nomes =  map(lambda p: p['nome'], lista_2)
print(list(so_nomes))

so_idades =  map(lambda p: p['idade'], lista_2)
print(sum(so_idades))


# Desefio: usando map retorne frasea <Nome> tem <idade> anos.
frases = list((map(lambda p: f'{p["nome"]} tem {p["idade"]} anos', lista_2)))
for i in frases:
    print(i)


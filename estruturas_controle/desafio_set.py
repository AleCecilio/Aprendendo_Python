PALAVRAS_PROIBUDAS = {'futebol', 'religiao', 'politica'}
textos = {
    'Joao gosta de futebol e politica',
    'A praia foi divertida',
}

for texto in textos:
    intersecao = PALAVRAS_PROIBUDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas: ', intersecao)
    else:
        print('Texto autorizado:', texto)

PALAVRAS_PROIBUDAS = ('futebol', 'religiao', 'politica')
textos = {
    'Joao gosta de futebol e politica',
    'A praia foi divertida',
}

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBUDAS:
            print('Texto possui pelo menos uma palvra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', texto)

'''
Exercício 6: Classificador de Texto
 Peça um texto do usuário.
 Conte número de palavras, letras e números.
 Converta palavras para maiúsculo.
 Substitua palavras proibidas (use set) por ***.
 Use comprehension para tamanho das palavras.
'''

def ler_texto():
    texto = input('Digite o texto: - >').strip()
    return texto


def contador_Palavras_Ltras_Num(texto):
    lista_palavra = []
    lista_letra = []
    lista_num = []
    for palavra in texto.split():
        if palavra.isdigit():
            lista_num.append(palavra)
        else:
            lista_palavra.append(palavra)
            for letra in palavra:
                if letra.isalpha():
                    lista_letra.append(letra)
            
    
    print('\nO texto tem:')
    print(f'{len(lista_palavra)} Palavras!')
    print(f'{len(lista_letra)} Letras')
    print(f'{len(lista_num)} Números')

    return lista_palavra


def converter_Maiusculas(lista):
    lista_maiuscula = [palavra.upper() for palavra in lista]
    texto = ' '.join(lista_maiuscula)
    print('\nPalavras em Maiúsculo:')
    print(texto)
    return lista_maiuscula


def palavras_Proibidas(lista):
    proibidas = {'burro', 'idiota', 'droga', 'besta', 'maldito'}
    censura = [palavra if palavra.lower() not in proibidas else '***' for palavra in lista]
    texto = ' '.join(censura)
    print('\nTexto Censurado:')
    print(texto)
    return censura


def tamanho_Palavras(lista):
    tam = [len(p) for p in lista]
    max_len = max(len(p) for p in lista)
    print('\nTamanho das Palvras:')
    for i in range(len(lista)):
        print (f'{lista[i].ljust(max_len)}: {tam[i]} letras')


if __name__ == '__main__':
    texto = ler_texto()
    lista_palavra = contador_Palavras_Ltras_Num(texto)
    lista_palavra = converter_Maiusculas(lista_palavra)
    lista_palavra = palavras_Proibidas(lista_palavra)
    tamanho_Palavras(lista_palavra)
    print('\n')
    
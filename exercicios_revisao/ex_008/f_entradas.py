import re

# --- Verica Números Inteiros --- 
def verifica_Int(prompt, min_val=None, max_val=None):
    while True:
        try:
            valor = int(input(prompt))
            if (min_val is not None and valor < min_val) or (max_val is not None and valor > max_val):
                print(f'Digite um número entre {min_val} e {max_val}.')
                continue
            return valor
        except ValueError:
            print('Digite um número válido!')


# --- Verifica Float ---
def verificar_Float(prompt):
    while True:
        try:
            valor = float(input(prompt)) 
            break
        except ValueError:
            print('Digite um valor válido')
    
    return valor


# --- Vefica se a String é Válida ---
def verifica_String(prompt):
    string = input(prompt).strip()
    while string == '':
        print(f'o campo não pode estar vazio!!!')
        string = input(prompt).strip()
    return string

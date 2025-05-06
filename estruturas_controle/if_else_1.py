#!python 

def Conceitos_Notas(valor):
    nota = float(valor)
    if nota > 10:
        return "A nota deve estar entre 0 e 10!"
    elif nota >= 9.1:
        return 'A'
    elif nota >= 8.1:
        return 'A-'
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1 :
        return 'B-'
    elif nota >= 5.1 :
        return 'C'
    elif nota >= 4.1 :
        return 'C-'
    elif nota >= 3.1 :
        return 'D'
    elif nota >= 2.1 :
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else: 
        return "A nota deve estar entre 0 e 10!"
    

if __name__ == '__main__':
    nota = input('Digite a Nota: ')
    print(Conceitos_Notas(nota))
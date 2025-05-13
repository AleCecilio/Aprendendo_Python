'''
Meu Código
def dias_semana_fds(dia):
    dias = {
        1 : 'Domingo',
        2 : 'Segunda', 
        3 : 'Terca',
        4 : 'Quarta',
        5 : 'Quinta',
        6 : 'Sexta',
        7 : 'Sabado',
    }
    return dias.get(dia, '**invalido**')

if __name__ == '__main__':
    for dia in range(0,8):
        if dia == 1 or dia == 7:
            print(f'{dia} : {dias_semana_fds(dia)} : Final de Semna')
        elif dia == 2 or dia == 3 or dia == 4 or dia == 5 or dia == 6:
            print(f'{dia} : {dias_semana_fds(dia)} : Dia Util')
        else:
            print(f'{dia} : {dias_semana_fds(dia)}')
'''

# Codigo do Curso
def get_tipo_dias(dia):
    dias = {
        1 : 'Final de Semna',
        2 : 'Dia Da Semana', 
        3 : 'Dia Da Semana',
        4 : 'Dia Da Semana',
        5 : 'Dia Da Semana',
        6 : 'Dia Da Semana',
        7 : 'Final de Semna',
    }
    return dias.get(dia, '**invalido**')

if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia} : {get_tipo_dias(dia)}')

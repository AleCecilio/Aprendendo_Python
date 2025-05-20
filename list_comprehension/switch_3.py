def get_tipo_dia(dia):
    dias = {
        (1, 7) : 'Fim De Semana',
        tuple(range(2, 7)) : 'Dia de Semana',
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, '** Dia Inválido **')


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f'{dia} : {get_tipo_dia(dia)}')

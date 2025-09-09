from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias
indice = filter(lambda i: mdays[i] == 31, [i for i in range(1,13)])

meses_31 = map(lambda i: month_name[i], indice)

juntar_meses =  reduce(lambda todos, mes_31: f'{todos}\n - {mes_31}',
                            meses_31, 'Meses com 31 dias:')

print(juntar_meses)

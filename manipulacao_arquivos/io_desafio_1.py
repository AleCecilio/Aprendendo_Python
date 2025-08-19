import csv
from urllib import request
import sys

sys.stdout.reconfigure(encoding='utf-8')

def read(url):
    with request.urlopen(url) as entrada:
        print('Baixando o CSV..')
        dados = entrada.read().decode('latin1')
        print('Dowload Completo!')
        for cidade in csv.reader(dados.splitlines()):
            print(f'{cidade[8]} : {cidade[3]}')



if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')

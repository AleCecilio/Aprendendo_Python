from pacote_loja import Vendedor, Cliente
from datetime import datetime

def main():
    cavaleiro_negro = Vendedor('Cavaleiro Negro', 45, 2000.00)
    rei_arthur = Vendedor('Rei Arthur', 33, 1975.83)
    brian = Cliente('Brian', 13)
    compra1 = (cavaleiro_negro, datetime(2001, 9, 11), 135.99)
    compra2 = (cavaleiro_negro, datetime(2004, 3, 10), 445.75)
    compra3 = (rei_arthur, datetime.now(), 666)
    brian.registrar_compra(compra1)
    brian.registrar_compra(compra2)
    brian.registrar_compra(compra3)

    print('--- Vendedores ---')
    print(cavaleiro_negro)
    print(rei_arthur)

    print(f'--- Informações do Cliente ---')
    print(brian)
    print(f'Ultima compra em: {brian.get_data_ultima_compra()}!')
    print(f'É', 'adulto!' if brian.is_Adulto() else 'menor de idade')
    print(f'Número de Compras: {len(brian.compras)}')
    print(f'Valor Total das Compras: R${brian.total_compras()}')
    

if __name__ == '__main__':
    main()
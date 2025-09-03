from .pessoa import Pessoa 
from .compra import Compra

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome,idade)
        self.compras = []

    def registrar_compra(self, compra):
        self.compras.append(Compra(*compra))

    def get_data_ultima_compra(self):
        return None if not self.compras else \
            sorted(self.compras, key=lambda compra: compra.data)[-1].data
    
    def total_compras(self):
        return float(sum(compra.valor for compra in self.compras)) \
            if self.compras else None

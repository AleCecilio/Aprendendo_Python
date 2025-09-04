class Humano:
    #atributo de classe 
    especie = 'Homo Sapiens'
    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensus', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Home {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neanderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    # HomoSapiens.das_cavernas(jose)
    grokn = Neanderthal('Grokn')
    
    print(f'Ecolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da intancia): {", ".join(jose.especies())}')
    print(f'HomoSapiens Evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal Evoluido? {Neanderthal.is_evoluido()}')
    print(f'José evoluido? {jose.is_evoluido()}')
    print(f'Grokn evoluido? {grokn.is_evoluido()}')

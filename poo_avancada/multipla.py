class Animal: 
    @property
    def capacidades(self):
        return('dormir', 'comer', 'beber')


class Homem(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('amar', 'falar', 'estududar')


class Arannha(Animal):
    @property
    def capacidades(self):
        return super().capacidades + ('fazer teia', 'andar pelas paredes')


class HomemAranha(Homem, Arannha):
    @property
    def capacidades(self):
        return super().capacidades + ('bater em bandidos', 'atirar teias entre prédios')
    
    
if __name__ == '__main__':
    john = Homem()
    print(f'Jhn: {john.capacidades}')

    arannha = Arannha()
    print(f'Aranha: {arannha.capacidades}')

    peter = HomemAranha()
    print(f'Peter Parker {peter.capacidades}')

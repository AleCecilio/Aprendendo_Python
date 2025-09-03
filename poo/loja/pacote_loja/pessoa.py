class Pessoa: 
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}'

    def is_Adulto(self):
        eh_Adulto = 18
        return (self.idade or 0) > eh_Adulto
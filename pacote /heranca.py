# toda class se nao declarada herança vai herdar de object
class MinhaClasse(object):
    pass


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf


p1 = PessoaFisica('111', 'matheus', '23')
print(p1.cpf)
print(p1.nome)
print(p1.idade)

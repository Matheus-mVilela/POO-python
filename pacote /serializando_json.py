import json


class Contato:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    @property
    def nome_completo(self):
        return self.nome, self.sobrenome


n = Contato('Matheus', 'Vilela')
print(json.dumps(n.__dict__))


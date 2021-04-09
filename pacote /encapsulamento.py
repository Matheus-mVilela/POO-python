class P:
    def __init__(self, valor):
        self.valor = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            print('Valor precisa ser superior a 0')


p = P(10)
print(p.valor)
p.valor = 3
print(p.valor)


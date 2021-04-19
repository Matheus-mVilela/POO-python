"""
def modifica(funcao):
    def subitrair(a, b):
        return a - b

    return subitrair

#o decorator esta modificando a função soma
@modifica
def soma(a, b):
    return a + b
"""


def modifica(funcao):
    def somar_par(a, b):
        if a % 2 == 0 or b % 2 == 0:
            return a + b
        return a - b

    return somar_par


@modifica
def somar(a, b):
    return a + b

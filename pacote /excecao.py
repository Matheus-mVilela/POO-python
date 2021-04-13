class Pares(list):
    def append(self, inteiro):
        if not isinstance(inteiro, int):
            raise TypeError('Somente inteiros')
        if inteiro % 2:
            raise ValueError('Somente numeros pares')

        super().append(inteiro)


# li = Pares()
# li.append(10)
# li.append(2)
# print(li)


def excecao():
    raise Exception('exececao')


def exececao2():
    try:
        excecao()
    except:
        print('Print da excecao')


# exececao2()


def divisao(divisor):
    try:
        if divisor == 13:
            raise ValueError('13 nao é numero valido')
        return 10 / divisor
    except ZeroDivisionError:
        return 'Divisao por 0 nao permitida'
    except TypeError:
        return 'Entre com valor númerico'
    except ValueError:
        return 'Numero nao conpativel'
        raise
    else:
        print('Nao ocorreu nenhuma excecao')
    finally:
        print('Sempre sera executado')


# print(divisao(13))


class Transacaoinvalida(Exception):
    def __init__(self, saldo, valor):
        super().__init__('soldo abaixo de R${}'.format(valor))
        self.valor = valor
        self.saldo = saldo

    def excecao(self):
        return self.valor - self, saldo


raise Transacaoinvalida(20, 10)

from importar import Quadrado


class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 10
        self.y = 20

    def __str__(self):
        return f'{self.x}, {self.y}'


class MinhaClasse:
    def __init__(self, n):
        self.n = n

    def foo(self):
        self.n += 1

    def reset(self):
        self.n = 0


if __name__ == '__main__':
    p = Ponto(100, 200)
    print('-->', p)
    print(p.x, p.y)
    # p.reset()
    Ponto.reset(p)
    print(p.x, p.y)

    obj = MinhaClasse(10)
    obj.foo()
    obj.reset()
    print(obj.n)

    # função importada da file importar

    p = Quadrado(5)
    p.perimetro()
    p.area()
    print(p.perimetro())
    print(p.area())

li = [1, 2, 3, 4, 5]

print(li)
li.append(5)
print(li)


# sobreescrevendo o metodo append para ele aceitar multiplas entradas.
class Lista(list):
    def append(self, *args):
        self.extend(args)


li = Lista()
li.append(1)
print(li)
li.append(2, 3, 4, 5, 6)
print(li)


def funcao(*args):
    print(args)


funcao(1, 2, 3)


def funcao2(**kwargs):
    print(kwargs)


funcao2(nome='matheus', idade=23, linguagem='python')

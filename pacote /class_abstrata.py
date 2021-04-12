from abc import ABCMeta, abstractmethod


class SuperClass(metaclass=ABCMeta):
    @abstractmethod
    def fazer_algo(self):
        pass

    # @abstractmethod
    # def fazer_outra_coisa(self):
    #     pass


class SubClass(SuperClass):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def fazer_algo(self):
        if self.x > self.y:
            print(self.x, 'maior que', self.y)
        else:
            print(self.y, 'maior que', self.x)


c = SubClass(1, 2)
c.fazer_algo()


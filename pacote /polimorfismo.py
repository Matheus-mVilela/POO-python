import math


class Forma:
    def __init__(self):
        print('Contrutor da forma')

    def area(self):
        print('Area da forma')

    def perimetro(self):
        print('perimetro da forma')

    def desc(self):
        print('Descrição da forma')


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

    def desc(self):
        print('Para se calcular area e perimetro de circulo precisamos do PI')


quad = Quadrado(4)
print(quad.area())
print(quad.perimetro())

cir = Circulo(3)
print('Area: %f' % cir.area())
print('Perimetro: %f' % cir.perimetro())
cir.desc()


class AudioFile:
    def __init__(self, filename):

        if not filename.endswith(self.txt):
            raise Exception('Formato nao encontrado')

        self.filename = filename


class Mp3File(AudioFile):
    ext = 'mp3'

    def play(self):
        print('Tocando mp3')


class WavFile(AudioFile):
    ext = 'wav'

    def play(self):
        print('Tocando wav')


class OggFile(AudioFile):
    ext = 'ogg'

    def play(self):
        print('Tocando ogg')

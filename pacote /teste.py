import unittest


class NumerosRomanos:
    def __init__(self, numeros_romanos):
        self.numeros_romanos = numeros_romanos
        self.digito = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 5, 'I': 1}

    def converter_para_decimal(self):
        val = 0
        for char in self.numeros_romanos:
            val += self.digito[char]

        return val


# class de teste
# assertEqual compara os numeros passado, com o valor convertido na def converter_para decimal


class TestNumerosRomanos(unittest.TestCase):
    def test_mil(self):
        value = NumerosRomanos('M')
        self.assertEqual(1000, value.converter_para_decimal())

    def test_quinhentos(self):
        value = NumerosRomanos('D')
        self.assertEqual(500, value.converter_para_decimal())

    def test_cem(self):
        value = NumerosRomanos('C')
        self.assertEqual(100, value.converter_para_decimal())

    def test_cinquenta(self):
        value = NumerosRomanos('L')
        self.assertEqual(50, value.converter_para_decimal())

    def test_cinco(self):
        value = NumerosRomanos('X')
        self.assertEqual(5, value.converter_para_decimal())

    def test_um(self):
        value = NumerosRomanos('I')
        self.assertEqual(1, value.converter_para_decimal())

    # assertTrue e assertFalse verifica se se os valores passados na def
    # converter_para_deimal são iguais 0 e maior que 0 respectivamente.
    def test_vazio(self):
        value = NumerosRomanos('')
        self.assertTrue(value.converter_para_decimal() == 0)
        self.assertFalse(value.converter_para_decimal() > 0)


if __name__ == '__main__':
    unittest.main()


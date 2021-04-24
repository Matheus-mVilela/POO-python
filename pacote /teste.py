import unittest


class NumerosRomanos:
    def __init__(self):
        self.digito = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 5, 'I': 1}

    def converter_para_decimal(self, numeros_romanos):
        val = 0
        for char in numeros_romanos:
            val += self.digito[char]

        return val


# class de teste
# assertEqual compara os numeros passado, com o valor convertido na def converter_para decimal


class TestNumerosRomanos(unittest.TestCase):
    def setUp(self):
        self.cnr = NumerosRomanos()

    def test_mil(self):
        self.assertEqual(1000, self.cnr.converter_para_decimal('M'))

    def test_quinhentos(self):
        self.assertEqual(500, self.cnr.converter_para_decimal('D'))

    def test_cem(self):
        self.assertEqual(100, self.cnr.converter_para_decimal('C'))

    def test_cinquenta(self):
        self.assertEqual(50, self.cnr.converter_para_decimal('L'))

    def test_cinco(self):
        self.assertEqual(5, self.cnr.converter_para_decimal('X'))

    def test_um(self):
        self.assertEqual(1, self.cnr.converter_para_decimal('I'))

    # assertTrue e assertFalse verifica se se os valores passados na def
    # converter_para_deimal são iguais 0 e maior que 0 respectivamente.
    def test_vazio(self):
        self.assertTrue(self.cnr.converter_para_decimal() == 0)
        self.assertFalse(self.cnr.converter_para_decimal() > 0)


if __name__ == '__main__':
    unittest.main()


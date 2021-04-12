class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    @classmethod
    def de_str(cls, data_str):
        dia, mes, ano = map(int, data_str.split('-'))
        data = cls(dia, mes, ano)
        return data

    @staticmethod
    def is_data_valid(data_str):
        dia, mes, ano = map(int, data_str.split('-'))
        data = cls(dia, mes, ano)

        return dia <= 31 and mes <= 12 and ano <= 2020


data = Data(10, 10, 10)
data1 = Data.de_str('10-10-2020')
print(data1)
vdd = Data.is_data_valid('10-10-2020')
print(vdd)

# toda class se nao declarada herança vai herdar de object
class MinhaClasse(object):
    pass


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, idade):
        Pessoa.__init__(self, nome, idade)
        self.cpf = cpf


class Funcionario:
    def __init__(self, nome, salario, cpf):
        self.nome = nome
        self.salario = salario
        self.cpf = cpf

    def get_bonificacao(self):
        return self.salario * 0.20


# Palavra reservada super chama o metodo da super class então quando alterar a superclass altera a subclass.
class Gerente(Funcionario):
    def __init__(self, nome, salario, cpf, senha):
        super().__init__(nome, salario, cpf)
        self.senha = senha

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000


# Herança multipla
class Relogio:
    def __init__(self, hora, minu, seg, *args, **kwargs):
        super(Relogio, self).__init__(*args, **kwargs)
        self.hora = hora
        self.minu = minu
        self.seg = seg

    def ajustar_hora(self, hora, minu, seg):
        self.hora = hora
        self.minu = minu
        self.seg = seg

    def __str__(self):
        return (
            '{0:02d}:{1:02d}:{2:02d}'.format(self.hora, self.minu, self.seg)
            + ','
            + super(Relogio, self).__str__()
        )

    def tick(self):
        if self.seg == 59:
            self.seg += 0
            if self.minu == 59:
                self.minu = 0
                if self.hora == 23:
                    self.hora = 0
                else:
                    self.hora += 1
            else:
                self.minu += 1
        else:
            self.seg += 1


rel = Relogio(23, 59, 59)
print(rel)
rel.tick()
print(rel)


class Calendario:

    meses = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    def __init__(self, dia, mes, ano, *args, **kwargs):
        super(Calendario, self).__init__(*args, **kwargs)
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def ajustar_data(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return '{0:02d}/{1:02d}/{2:4}'.format(self.dia, self.mes, self.ano)

    def dia_seg(self):
        dia_max_mes = Calendario.meses[self.mes - 1]

        if self.dia == dia_max_mes:
            self.dia = 1
            if self.mes == 12:
                self.mes = 1
                self.ano += 1
            else:
                self.mes += 1
        else:
            self.dia += 1


cal = Calendario(10, 3, 2020)
print(cal)
cal.dia_seg()
print(cal)


class CalendarioRelogio(Relogio, Calendario):
    def __init__(self, hora, minu, seg, dia, mes, ano):
        super(CalendarioRelogio, self).__init__(
            hora=hora, minu=minu, seg=seg, dia=dia, mes=mes, ano=ano
        )

    def __str__(self):
        return super(CalendarioRelogio, self).__str__()

    def tick(self):
        hora_anterior = self.hora
        Relogio.tick(self)
        if self.hora < hora_anterior:
            self.dia_seg()


cal_rel = CalendarioRelogio(10, 10, 10, 10, 10, 2010)
print(cal_rel)
cal_rel.tick()
print(cal_rel)

print(CalendarioRelogio.mro())


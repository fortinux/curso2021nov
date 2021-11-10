import datetime

class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        # inicializa los parámetros
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

    @classmethod
    def valor_ticket(cls, valor):
        cls.valor_ticket = valor

    @staticmethod
    def dia_evento(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True

festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')
festival2 = FestivalMusical('Primavera sound', 'SP', 'Pop')


print(festival2.nombre, festival2.pais, festival2.estilo_musical)
print(festival1.nombre.upper())
festival2.nombre = ('Benicassim')
print(festival2.nombre)
del festival1
print(festival1)

class Paises:
    pass




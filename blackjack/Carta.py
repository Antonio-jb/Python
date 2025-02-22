class Carta:
    def __init__(self, valor, nombre, palo):
        self.valor = valor
        self.nombre = nombre
        self.palo = palo

    def __repr__(self):
        return f"{self.nombre}"
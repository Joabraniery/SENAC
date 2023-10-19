import math

class FiguraPlana:
    def calcular_area(self):
        pass

class Triangulo(FiguraPlana):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

class Retangulo(FiguraPlana):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

class Circulo(FiguraPlana):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

class Losango(FiguraPlana):
    def __init__(self, diagonal_maior, diagonal_menor):
        self.diagonal_maior = diagonal_maior
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        return 0.5 * self.diagonal_maior * self.diagonal_menor

class Paralelogramo(FiguraPlana):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Trapezio(FiguraPlana):
    def __init__(self, base_maior, base_menor, altura):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def calcular_area(self):
        return 0.5 * (self.base_maior + self.base_menor) * self.altura

# Exemplo de uso:
triangulo = Triangulo(5, 4)
print("Área do Triângulo:", triangulo.calcular_area())

retangulo = Retangulo(6, 8)
print("Área do Retângulo:", retangulo.calcular_area())

circulo = Circulo(3)
print("Área do Círculo:", circulo.calcular_area())

losango = Losango(6, 8)
print("Área do Losango:", losango.calcular_area())

paralelogramo = Paralelogramo(7, 5)
print("Área do Paralelogramo:", paralelogramo.calcular_area())

trapezio = Trapezio(5, 3, 4)
print("Área do Trapézio:", trapezio.calcular_area())

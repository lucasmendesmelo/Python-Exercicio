from triangulo import Triangulo


ladoA = float(input("Informe a primeira medida de um triangulo: "))

ladoB = float(input("Informe a segunda medida de um triangulo: "))

ladoC = float(input("Informe a terceira medida de um triangulo: "))

triangulo = Triangulo(ladoA, ladoB, ladoC)

perimetro = triangulo.calcularPerimetro()
maiorLado = triangulo.maiorLado()

print("O perimetro é: ", perimetro)
print("O maior lado é: ", maiorLado)
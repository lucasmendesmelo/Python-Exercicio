class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
        
        
    def calcularPerimetro(self):
        
       return self.ladoA + self.ladoB + self.ladoC
            
    def maiorLado(self):
    
      return max(self.ladoA, self.ladoB, self.ladoC)    
     
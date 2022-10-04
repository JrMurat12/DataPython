class Expo:
    def __init__(self, base, expoente):
        self.base = base
        self.expoente = expoente

    def Calcular(self):
        fixo = self.base
        for i in range (self.expoente-1):
            self.base = (self.base * fixo)
        return self.base
   
          
basei = int(input("Digite o número da base: "))
expoentei = int(input("Digite o número do expoente: "))
obj1 = Expo(basei, expoentei) 
print (obj1.base)
print (obj1.expoente)
print (obj1.Calcular())
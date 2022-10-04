class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def Soma(self):
        return self.valor1 + self.valor2
        
    def Subtrair(self):
        return self.valor1 - self.valor2
        
    def Multi(self):
        return self.valor1 * self.valor2
        
    def Div(self):
        return self.valor1 / self.valor2
    
privalor = float(input("Digite o primeiro número: "))
segvalor = float(input("Digite o segundo número: "))
obj1 = Calculadora(privalor, segvalor)
i = int(input("Digite a operação que deseja realizar: "))
match i:
    case 1:
        print(obj1.Soma())
    case 2:
        print(obj1.Subtrair())
    case 3:
        print(obj1.Multi())
    case 4:
        print(obj1.Div())
        
class LetraGrande:
    def Maiuscula (self, frase):
        return frase.upper()

frasex = str(input("Digite o número da base: "))
obj1 = LetraGrande()
print (frasex)
print(obj1.Maiuscula(frasex))



i=0
soma=0
sub=0
for i in range (5):
    num = int(input("Digite o valor: "))
    if (num >= 5):
        soma+=1
    else:
        sub+=1

print("Quantidade de numeros maiores que 5 é: " + str(soma))
print("Quantidade de numeros menores que 5 é: " + str(sub))
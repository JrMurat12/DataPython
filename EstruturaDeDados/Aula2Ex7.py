num = int(input("Digite números de valores a informar: "))
soma = 0
sub=0
media = 0
cont=0
for i in range (num):
    valor = int(input("Digite o valor: "))
    if (valor > 0):
        soma+=valor
        cont+=1
    else:
        sub+=valor

media = soma / cont
print ("A média é: " + str(media))
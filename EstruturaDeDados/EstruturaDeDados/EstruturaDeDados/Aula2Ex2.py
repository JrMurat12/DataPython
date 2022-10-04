num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num2 > num1:
    for num in range (num2 - num1):
        print (num + num1)
else:
    for n in range (num1 - num2):
        print (n + num2)
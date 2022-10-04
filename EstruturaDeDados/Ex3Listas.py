list_num = []
num_escolhido = 0
for i in range(10):
    list_num.append(input("Digite um número: "))
while True:
    num_escolhido = (input("Escolha o número que deseja: "))
    if num_escolhido in list_num:
        print("Este número está na lista! E aparece " + str(list_num.count(num_escolhido)) + " vezes")
        break
    else:
        print("Número não está na lista")


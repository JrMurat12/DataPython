list_num = []
contneg = 0
for i in range(12):
    num = int(input("Digite um número: "))
    list_num.append(num)
    if (num < 0):
        contneg+=1
        list_num.remove(num)
    else:
        list_num.remove(num)
        list_num.append(num)
print(list_num)
print("A lista possui " + str(contneg) + " números negativos")
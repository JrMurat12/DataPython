list_num = []
for i in range(12):
    num = int(input("Digite um número: "))
    list_num.append(num)
    if (num < 0):
        list_num.remove(num)
    else:
        list_num.remove(num)
        list_num.append(num)
print(list_num)
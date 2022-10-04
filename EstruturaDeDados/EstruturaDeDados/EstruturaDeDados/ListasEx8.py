list_num = []

for i in range(10):
    num = int(input("Digite um número: "))
    list_num.append(num)
    if (num > 0 and i%2 == 1):
        list_num.remove(num)
        list_num.append(num)
    else:
        list_num.remove(num)
print(sum(list_num))

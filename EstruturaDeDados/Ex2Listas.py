list_num = []
num=0
for i in range(5):
    num = int(input("Digite um número: "))
    while num < 0:
        num = int(input("Digite um número: "))
    list_num.append(num)
    if (num > 0 and i%2 == 1):
        list_num.remove(num)
        list_num.append(num)
    else:
        list_num.remove(num)
print(list_num)
print(sum(list_num))
#Listas começam na posição zero que é par

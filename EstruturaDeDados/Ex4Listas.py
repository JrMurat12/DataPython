list_num = []
reverse_list = []
matriz_list = []
for i in range(10):
    list_num.append(input("Digite um número: "))
    
reverse_list = list_num.copy()
reverse_list.reverse() 
print(list_num)
print(reverse_list)

for i in range(10):
    if list_num [i]!=reverse_list[i]:
        matriz_list.append('_')
    else:
        matriz_list.append(list_num[i])

print(matriz_list)

        




import operator

list_num = []

for i in range(15):
    list_num.append(int(input("Digite um número: ")))
    mult_list = [2] * len(list_num)
    result = list(map(operator.mul, list_num, mult_list))
print(result)

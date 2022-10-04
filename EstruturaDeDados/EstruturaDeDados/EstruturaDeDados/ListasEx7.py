list_num = []
num=0

for i in range(100):
    n=i+1
    list_num.append(n)
    if(n%2 == 0):
        list_num.remove(n)
        list_num.append(n)
    else:
        list_num.remove(n)
print(list_num)

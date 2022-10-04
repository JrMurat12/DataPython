tamanho=0
palindromo = []
num_escolhido = 0
tamanho = int(input("Digite o tamanho do número: "))
for i in range(tamanho):
    palindromo.append(input("Digite o valor separadamente: "))
    
reverse_list = palindromo.copy()
reverse_list.reverse() 

if palindromo==reverse_list:
    print("É um palíndromo!!!")
else:
    print("Não é um palíndromo!!!")
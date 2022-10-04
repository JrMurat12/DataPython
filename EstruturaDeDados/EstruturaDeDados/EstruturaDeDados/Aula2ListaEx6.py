soma_altura_mulher = 0
soma_altura_homem = 0
media_altura_mulher = 0
media_altura_homem = 0
cont_mulher = 0
cont_homem = 0
guarda_maior = 0
guarda_menor = 100

for i in range (15):
    altura = float(input("Digite a altura: "))
    sexo = int(input("Digite o sexo: "))

    if altura > guarda_maior:
        guarda_maior = altura
        sexo_alto = sexo
    if altura < guarda_menor:
        guarda_menor = altura
    if sexo == 2:
        soma_altura_mulher+=altura
        cont_mulher+=1
        media_altura_mulher = soma_altura_mulher / cont_mulher
    else:
        soma_altura_homem+=altura
        cont_homem += 1
        media_altura_homem = soma_altura_homem / cont_homem

print ("A menor altura do grupo é: " + str(guarda_menor))
print ("A média da altura das mulheres é: " + str(media_altura_mulher))
print ("Número de homens é: " + str(cont_homem))
print ("Sexo da pessoa mais alta é: " + str(sexo_alto))




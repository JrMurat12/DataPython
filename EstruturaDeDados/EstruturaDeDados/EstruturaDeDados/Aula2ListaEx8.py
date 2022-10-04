num_alunos = int(input("Digite o número de alunos: "))
for i in range (num_alunos):
    quant_disc = int(input("Digite o número de disciplinas do aluno " + str(i + 1) + " : "))
    notas = 0
    for n in range (quant_disc):
        notas += float(input("Digite a nota da " + str(n + 1) + "ª" + " disciplina: "))
        if(notas < 0):
            print("Nota inválida!!!")
            break
        else:
            media = notas / float(quant_disc)
    if(media < 0):
        print("Nota inválida!!!")
    elif(media < 5):
        print("A média do aluno " + str(i) + " foi de: " + str(media) + ". Aluno reprovado!!!")
    elif(media >= 5 and media < 10):
        print("A média do aluno " + str(i) + " foi de: " + str(media) + ". Aluno provado!!!")
    else:
        print("Aluno destaque!!! Ganhou bolsa de 100% na pós-graduação")
